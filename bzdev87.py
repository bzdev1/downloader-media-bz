import os import sys from time import sleep, time from datetime import datetime, timedelta from rich.console import Console from rich.panel import Panel from rich.prompt import Prompt from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn from rich.table import Table import yt_dlp

console = Console() DOWNLOAD_DIR = "/storage/emulated/0/bzdown" LICENSE_FILE = "licenses.txt" LICENSE_DURATION_DAYS = 7 WHATSAPP_CONTACT = "https://wa.me/6287825946251"

def show_banner(): banner = """ [bold red] ██████  ███████ ███████ ██████  ███████ ██    ██ ███████ ██    ██  ██   ██ ██      ██      ██   ██ ██       ██  ██  ██       ██  ██   ██   ██ █████   █████   ██████  █████     ████   █████     ████   ██   ██ ██      ██      ██      ██         ██    ██         ██  
██████  ███████ ███████ ██      ███████    ██    ███████    ██ 
[/bold red]
[bold cyan]>>> bzdev87 Social Media Downloader - All in One <<<[/bold cyan]
""" console.print(Panel(banner, style="bold green"))

def create_download_folder(): if not os.path.exists(DOWNLOAD_DIR): os.makedirs(DOWNLOAD_DIR) console.print(f"[green]Folder dibuat:[/green] {DOWNLOAD_DIR}")

def check_license(): if not os.path.exists(LICENSE_FILE): activate_license() with open(LICENSE_FILE, 'r') as f: start_time = float(f.read().strip()) if time() - start_time > LICENSE_DURATION_DAYS * 86400: console.print("[bold red]Lisensi Anda sudah kadaluarsa.[/bold red]") console.print(f"[bold yellow]Silakan hubungi admin untuk aktivasi:[/bold yellow] {WHATSAPP_CONTACT}") sys.exit()

def activate_license(): with open(LICENSE_FILE, 'w') as f: f.write(str(time())) console.print("[bold green]Lisensi aktif selama 7 hari.[/bold green]")

def menu(): table = Table(title="[bold cyan]MENU UTAMA[/bold cyan]", show_header=True, header_style="bold magenta") table.add_column("No", style="bold yellow") table.add_column("Aksi", style="bold white") table.add_row("1", "Download Video") table.add_row("2", "Download MP3") table.add_row("3", "Download Gambar") table.add_row("4", "Buka Folder Download") table.add_row("5", "Info Developer") table.add_row("6", "Bantuan / Cara Pakai") table.add_row("7", "Keluar") console.print(table)

def download_media(url, media_type): ext_map = { 'video': '%(title)s.%(ext)s', 'audio': '%(title)s.%(ext)s', 'image': '%(title)s.%(ext)s' } format_map = { 'video': 'best', 'audio': 'bestaudio', 'image': 'best' } ydl_opts = { 'outtmpl': os.path.join(DOWNLOAD_DIR, ext_map[media_type]), 'format': format_map[media_type], 'noplaylist': True, 'quiet': True, 'no_warnings': True, 'progress_hooks': [hook], } if media_type == 'audio': ydl_opts['postprocessors'] = [{ 'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192', }]

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
except Exception as e:
    console.print(f"[bold red]Gagal download:[/bold red] {e}")

def hook(d): if d['status'] == 'finished': console.print(f"\n[bold green]Selesai:[/bold green] {d['filename']}")

def info_dev(): console.print(Panel(f""" [bold cyan]Developer:[/bold cyan] BZOneDev87 [bold cyan]Github:[/bold cyan] github.com/bzonedev87 [bold cyan]Tools:[/bold cyan] yt-dlp + rich + Termux Ready """, title="INFO DEVELOPER", style="bold green"))

def bantuan(): console.print(Panel(""" [bold yellow]Cara pakai:[/bold yellow]

1. Pilih menu yang tersedia


2. Masukkan URL dari media:

YouTube

TikTok

Instagram

Facebook

Twitter / X

dan lainnya



3. File otomatis tersimpan di: ~/bzdown



Gunakan menu 'Buka Folder' untuk akses file hasil download. """, title="BANTUAN", style="bold blue"))

def run(): show_banner() create_download_folder() check_license()

while True:
    menu()
    pilihan = Prompt.ask("[bold yellow]Masukkan pilihan[/bold yellow]", choices=["1", "2", "3", "4", "5", "6", "7"])

    if pilihan in ["1", "2", "3"]:
        url = Prompt.ask("[cyan]Masukkan URL Media[/cyan]")
        jenis = "video" if pilihan == "1" else "audio" if pilihan == "2" else "image"
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            transient=True,
        ) as progress:
            task = progress.add_task("[green]Mendownload...", total=None)
            download_media(url, jenis)
            progress.update(task, completed=100)

    elif pilihan == "4":
        console.print(f"[blue]Folder penyimpanan media:[/blue] {DOWNLOAD_DIR}")
        if sys.platform.startswith("linux") or sys.platform == "darwin":
            os.system(f"xdg-open {DOWNLOAD_DIR} || termux-open {DOWNLOAD_DIR}")
        elif sys.platform == "win32":
            os.startfile(DOWNLOAD_DIR)

    elif pilihan == "5":
        info_dev()

    elif pilihan == "6":
        bantuan()

    elif pilihan == "7":
        console.print("[bold magenta]Sampai jumpa dan selamat mendownload![/bold magenta]")
        break

if name == "main": run()

