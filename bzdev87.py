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

# Tambahan fungsi utama (menu) bisa kamu tambah sendiri
if __name__ == "__main__":
    check_license()
    show_banner()
