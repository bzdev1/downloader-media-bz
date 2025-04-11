# bzdev87.py - Downloader Sosmed All-in-One
# Author: BZOneDev87
# Versi dengan Lisensi Publik & Developer + Animasi Pembuka

import os
import sys
from time import sleep
from datetime import datetime, timedelta
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

def create_download_folder():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

def animasi_pembuka():
    teks = "Membuka BZDev87 Downloader..."
    for i in teks:
        console.print(i, end="", style="bold cyan", justify="center")
        sleep(0.03)
    print()

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

def create_license(jenis="Publik"):
    expire = datetime.now() + timedelta(days=LICENSE_DURATION_DAYS)
    with open(LICENSE_FILE, "w") as f:
        f.write(f"{expire.timestamp()}\nLICENSE_TYPE={jenis.lower()}")
    console.print(f"[green]Lisensi {jenis} aktif sampai:[/green] {expire}")

def check_license():
    if not os.path.exists(LICENSE_FILE):
        console.print("[bold red]Lisensi tidak ditemukan![/bold red]")
        open_license = Prompt.ask("Ingin aktivasi lisensi sekarang? (y/n)", choices=["y", "n"])
        if open_license == "y":
            os.system(f"termux-open-url {WHATSAPP_CONTACT}")
        sys.exit()

    with open(LICENSE_FILE, "r") as f:
        content = f.read()
        try:
            lines = content.strip().split("\n")
            timestamp = float(lines[0])
            license_type = "publik"
            for line in lines:
                if line.startswith("LICENSE_TYPE="):
                    license_type = line.split("=")[-1]

            expire_time = datetime.fromtimestamp(timestamp)
            if datetime.now() > expire_time:
                console.print("[bold red]Lisensi sudah kedaluwarsa![/bold red]")
                os.remove(LICENSE_FILE)
                sys.exit()
            if license_type == "developer":
                console.print("[bold cyan]Developer License aktif - akses penuh[/bold cyan]")
            else:
                console.print("[bold green]Lisensi Publik aktif[/bold green]")
        except:
            console.print("[red]Format lisensi tidak valid.[/red]")
            os.remove(LICENSE_FILE)
            sys.exit()

def download_media(url):
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
        'progress_hooks': [hook],
        'quiet': True,
    }
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                  BarColumn(), transient=True) as progress:
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
    table.add_row("3", "Info Lisensi")
    table.add_row("4", "Keluar")
    console.print(table)

def info_lisensi():
    with open(LICENSE_FILE, "r") as f:
        lines = f.read().strip().split("\n")
        waktu = datetime.fromtimestamp(float(lines[0]))
        tipe = "Publik"
        for l in lines:
            if l.startswith("LICENSE_TYPE="):
                tipe = l.split("=")[-1].capitalize()
        console.print(f"[bold cyan]Tipe Lisensi:[/bold cyan] {tipe}")
        console.print(f"[bold cyan]Aktif Sampai:[/bold cyan] {waktu}")

def run():
    animasi_pembuka()
    check_license()
    create_download_folder()
    show_banner()

    while True:
        menu()
        pilihan = Prompt.ask("[bold yellow]Pilih opsi[/bold yellow]", choices=["1", "2", "3", "4"])

        if pilihan == "1":
            url = Prompt.ask("[cyan]Masukkan URL media[/cyan]")
            download_media(url)
        elif pilihan == "2":
            jenis = Prompt.ask("Jenis lisensi (Publik/Developer)", choices=["Publik", "Developer"])
            create_license(jenis)
        elif pilihan == "3":
            info_lisensi()
        elif pilihan == "4":
            console.print("[bold magenta]Sampai jumpa![/bold magenta]")
            break

if __name__ == "__main__":
    run()
