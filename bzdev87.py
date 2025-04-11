import os
import sys
import requests
import yt_dlp
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import Progress

console = Console()
LICENSE_FILE = "license.txt"
DOWNLOAD_FOLDER = "downloads"
WHATSAPP_CONTACT = "https://wa.me/6287825946251"

def show_banner():
    banner = """
██████╗ ███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗
██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝╚██╗ ██╔╝
██████╔╝█████╗  ██║   ██║██║  ██║█████╗   ╚████╔╝ 
██╔═══╝ ██╔══╝  ██║   ██║██║  ██║██╔══╝    ╚██╔╝  
██║     ███████╗╚██████╔╝██████╔╝███████╗   ██║   
╚═╝     ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝   
"""
    console.print(banner, style="bold magenta")

def create_download_folder():
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

def create_license(jenis):
    with open(LICENSE_FILE, "w") as f:
        f.write(f"LICENSE_TYPE={jenis}\n")
    console.print(f"[bold green]Lisensi {jenis} berhasil dibuat![/bold green]")

def download_media(url, mode):
    create_download_folder()
    output = os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s')

    if mode == "Video":
        ydl_opts = {
            'outtmpl': output,
            'format': 'bestvideo+bestaudio/best',
            'progress_hooks': [hook],
        }
    elif mode == "MP3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output,
            'progress_hooks': [hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    elif mode == "Gambar":
        try:
            r = requests.get(url)
            filename = os.path.join(DOWNLOAD_FOLDER, url.split("/")[-1])
            with open(filename, "wb") as f:
                f.write(r.content)
            console.print(f"[bold green]Gambar disimpan ke:[/bold green] {filename}")
            return
        except Exception as e:
            console.print(f"[bold red]Gagal download gambar:[/bold red] {e}")
            return
    else:
        console.print("[red]Mode tidak dikenal.[/red]")
        return

    try:
        with Progress() as progress:
            task = progress.add_task("[cyan]Mendownload...", total=None)
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

def check_license():
    if not os.path.exists(LICENSE_FILE):
        console.print("[bold red]Lisensi tidak ditemukan![/bold red]")
        open_license = Prompt.ask("Ingin aktivasi lisensi sekarang? (y/n)", choices=["y", "n"])
        if open_license == "y":
            os.system(f"termux-open-url {WHATSAPP_CONTACT}")
        sys.exit()

    with open(LICENSE_FILE, "r") as f:
        content = f.read()
        if "LICENSE_TYPE=developer" in content:
            console.print("[bold cyan]Developer License aktif - akses penuh[/bold cyan]")
        elif "LICENSE_TYPE=Publik" in content:
            console.print("[bold green]Lisensi Publik aktif[/bold green]")
        else:
            console.print("[bold red]Format lisensi tidak valid.[/bold red]")
            sys.exit()

def run():
    show_banner()
    check_license()
    create_download_folder()

    while True:
        menu()
        pilihan = Prompt.ask("[bold yellow]Pilih opsi[/bold yellow]", choices=["1", "2", "3"])

        if pilihan == "1":
            url = Prompt.ask("[cyan]Masukkan URL media[/cyan]")
            mode = Prompt.ask("Pilih jenis media", choices=["Video", "MP3", "Gambar"])
            download_media(url, mode)
        elif pilihan == "2":
            jenis = Prompt.ask("Jenis lisensi (Publik/Developer)", choices=["Publik", "Developer"])
            create_license(jenis)
        elif pilihan == "3":
            console.print("[bold magenta]Sampai jumpa![/bold magenta]")
            break

if __name__ == "__main__":
    run()
