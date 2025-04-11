# bzdev87.py - Downloader Sosmed All-in-One
# Author: BZOneDev87
# Versi: Final Revisi Lisensi Developer/Publik

import os
import sys
from datetime import datetime, timedelta
from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
import yt_dlp

console = Console()

DOWNLOAD_DIR = "/storage/emulated/0/bzdown"
LICENSE_FILE = "license.txt"
LICENSE_DURATION_DAYS = 7
WHATSAPP_CONTACT = "https://wa.me/6287825946251"

def check_license():
    if not os.path.exists(LICENSE_FILE):
        console.print("[bold red]Lisensi tidak ditemukan![/bold red]")
        open_license = Prompt.ask("Aktivasi lisensi sekarang? (y/n)", choices=["y", "n"])
        if open_license == "y":
            os.system(f"termux-open-url {WHATSAPP_CONTACT}")
        sys.exit()

    with open(LICENSE_FILE, "r") as f:
        content = f.read().strip()
        parts = content.split("|")
        if len(parts) != 2:
            console.print("[red]Format lisensi tidak valid.[/red]")
            os.remove(LICENSE_FILE)
            sys.exit()

        lisensi_type, timestamp = parts
        try:
            expire_time = datetime.fromtimestamp(float(timestamp))
            if datetime.now() > expire_time:
                console.print("[bold red]Lisensi sudah kedaluwarsa![/bold red]")
                os.remove(LICENSE_FILE)
                sys.exit()
            else:
                console.print(f"[green]Lisensi aktif:[/green] {lisensi_type} (sampai {expire_time})")
        except:
            console.print("[red]Gagal membaca lisensi.[/red]")
            os.remove(LICENSE_FILE)
            sys.exit()

def create_license(lisensi_type="Publik"):
    expire = datetime.now() + timedelta(days=LICENSE_DURATION_DAYS)
    with open(LICENSE_FILE, "w") as f:
        f.write(f"{lisensi_type}|{expire.timestamp()}")
    console.print(f"[green]Lisensi {lisensi_type} aktif sampai:[/green] {expire}")

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

def create_download_folder():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
        console.print(f"[green]Folder dibuat:[/green] {DOWNLOAD_DIR}")

def download_media(url):
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [hook],
    }

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Mendownload media...", total=None)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            progress.update(task, completed=100)
        except Exception as e:
            console.print(f"[bold red]Gagal download:[/bold red] {e}")

def hook(d):
    if d['status'] == 'finished':
        console.print(f"[bold green]Selesai:[/bold green] {d['filename']}")

def menu():
    table = Table(title="[bold cyan]MENU UTAMA[/bold cyan]", show_header=True, header_style="bold magenta")
    table.add_column("No", style="bold yellow")
    table.add_column("Aksi", style="bold white")
    table.add_row("1", "Download Media")
    table.add_row("2", "Buat Lisensi Baru")
    table.add_row("3", "Keluar")
    console.print(table)

def run():
    check_license()
    show_banner()
    create_download_folder()

    while True:
        menu()
        pilihan = Prompt.ask("[bold yellow]Pilih opsi[/bold yellow]", choices=["1", "2", "3"])

        if pilihan == "1":
            url = Prompt.ask("[cyan]Masukkan URL media[/cyan]")
            download_media(url)
        elif pilihan == "2":
            jenis = Prompt.ask("Jenis lisensi (Publik/Developer)", choices=["Publik", "Developer"])
            create_license(jenis)
        elif pilihan == "3":
            console.print("[bold magenta]Sampai jumpa![/bold magenta]")
            break

if __name__ == "__main__":
    run()
