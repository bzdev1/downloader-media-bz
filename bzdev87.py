# bzdev87.py - Downloader Sosmed All-in-One
# Author: BZOneDev87
# Versi Revisi dengan Lisensi 7 Hari

import os
import sys
from time import sleep, time
from datetime import datetime, timedelta
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
import yt_dlp

console = Console()

DOWNLOAD_DIR = "/storage/emulated/0/bzdown"
LICENSE_FILE = "licenses.txt"
LICENSE_DURATION_DAYS = 7
WHATSAPP_CONTACT = "https://wa.me/6287825946251"

def check_license():
    if not os.path.exists(LICENSE_FILE):
        console.print("[bold red]Lisensi tidak ditemukan![/bold red]")
        open_license = Prompt.ask("Ingin aktivasi lisensi sekarang? (y/n)", choices=["y", "n"])
        if open_license == "y":
            os.system(f"termux-open-url {WHATSAPP_CONTACT}")
        sys.exit()

    with open(LICENSE_FILE, "r") as f:
        timestamp = f.read().strip()
        try:
            expire_time = datetime.fromtimestamp(float(timestamp))
            if datetime.now() > expire_time:
                console.print("[bold red]Lisensi sudah kedaluwarsa![/bold red]")
                os.remove(LICENSE_FILE)
                sys.exit()
        except:
            console.print("[red]Format lisensi tidak valid.[/red]")
            os.remove(LICENSE_FILE)
            sys.exit()

def create_license():
    expire = datetime.now() + timedelta(days=LICENSE_DURATION_DAYS)
    with open(LICENSE_FILE, "w") as f:
        f.write(str(expire.timestamp()))
    console.print(f"[green]Lisensi aktif sampai:[/green] {expire}")

def show_banner():
    banner = """[bold red]
██████  ███████ ███████ ██████  ███████ ██    ██ ███████ ██    ██ 
██   ██ ██      ██      ██   ██ ██       ██  ██  ██       ██  ██  
██   ██ █████   █████   ██████  █████     ████   █████     ████   
██   ██ ██      ██      ██      ██         ██    ██         ██    
██████  ███████ ███████ ██      ███████    ██    ███████    ██    
[bold cyan]>>> bzdev87 Sosmed Downloader - MP4/MP3/IMG + Lisensi <<<[/bold cyan]
"""
    console.print(Panel(banner, style="bold green"))

def progress_bar(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "0%").strip()
        filename = d.get("filename", "file")
        console.print(f"[yellow]Mengunduh:[/yellow] {percent} - {filename}", end="\r")
    elif d["status"] == "finished":
        console.print(f"\n[green]Selesai:[/green] {d['filename']}")

def download_media(url, mode):
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    ydl_opts = {
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
        "quiet": True,
        "progress_hooks": [lambda d: progress_bar(d)],
    }

    if mode == "mp3":
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    elif mode == "img":
        ydl_opts["skip_download"] = True
        ydl_opts["writethumbnail"] = True
    else:
        ydl_opts["format"] = "best"

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        console.print(f"[bold red]Gagal mendownload:[/bold red] {e}")

def menu():
    while True:
        console.print("\n[bold cyan]Menu Pilihan:[/bold cyan]")
        table = Table(title="Downloader Menu")
        table.add_column("No", justify="center")
        table.add_column("Fitur")
        table.add_row("1", "Download Video (MP4)")
        table.add_row("2", "Download Audio (MP3)")
        table.add_row("3", "Download Gambar (Thumbnail)")
        table.add_row("0", "Keluar")
        console.print(table)

        choice = Prompt.ask("Pilih opsi", choices=["1", "2", "3", "0"])
        if choice == "0":
            console.print("[bold red]Keluar...[/bold red]")
            break

        url = Prompt.ask("Masukkan URL")
        if choice == "1":
            download_media(url, "mp4")
        elif choice == "2":
            download_media(url, "mp3")
        elif choice == "3":
            download_media(url, "img")

if __name__ == "__main__":
    check_license()
    show_banner()
    menu()
