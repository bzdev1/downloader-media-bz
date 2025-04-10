bzdev87.py

import os import sys import time from rich import print from rich.console import Console from rich.table import Table from rich.prompt import Prompt from rich.progress import Progress

console = Console() DOWNLOAD_FOLDER = "/sdcard/bzdownloader" LICENSE_FILE = "license.key" MAX_DOWNLOADS_FREE = 3 user_downloads = 0

Cek dan buat folder download

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

Fungsi verifikasi lisensi

def check_license(): if not os.path.exists(LICENSE_FILE): with open(LICENSE_FILE, "w") as f: f.write("BZDEV-2025-001\nBZDEV-2025-002")

user_license = Prompt.ask("[bold yellow]Masukkan kode lisensi untuk akses penuh[/bold yellow]")
with open(LICENSE_FILE, "r") as f:
    valid_keys = f.read().splitlines()

if user_license in valid_keys:
    print("[bold green]\n✔ Lisensi valid. Developer mode aktif!\n")
    return True
else:
    print("[bold red]\n✘ Lisensi tidak valid atau kosong.")
    print("[bold cyan]Hubungi developer: https://wa.me/6287825946251[/bold cyan]\n")
    return False

Tampilan judul

def show_banner(): os.system("clear") print(""" [bold green]╭────────────────────────────────────────────────────────────────────╮ │ ██████  ███████ ███████ ██████  ███████ ██    ██ ███████ ██    ██  │ │ ██   ██ ██      ██      ██   ██ ██       ██  ██  ██       ██  ██   │ │ ██   ██ █████   █████   ██████  █████     ████   █████     ████    │ │ ██   ██ ██      ██      ██      ██         ██    ██         ██     │ │ ██████  ███████ ███████ ██      ███████    ██    ███████    ██     │ │ >>> bzdev87 Social Media Downloader - All in One <<<               │ ╰────────────────────────────────────────────────────────────────────╯[/bold green] """)

Menu utama

def main_menu(is_developer=False): table = Table(title="[bold cyan]MENU UTAMA[/bold cyan]", show_lines=True) table.add_column("No", justify="center") table.add_column("Aksi") table.add_row("1", "Download Media") table.add_row("2", "Buka Folder Download") table.add_row("3", "Info Developer") table.add_row("4", "Bantuan / Cara Pakai") if is_developer: table.add_row("5", "[yellow]Developer Mode[/yellow]") table.add_row("6", "Keluar") else: table.add_row("5", "Keluar")

console.print(table)
pilihan = Prompt.ask("Masukkan pilihan", choices=["1", "2", "3", "4", "5", "6"] if is_developer else ["1", "2", "3", "4", "5"])
handle_choice(pilihan, is_developer)

Fungsi tiap menu

def handle_choice(pilihan, is_developer): global user_downloads if pilihan == "1": if not is_developer and user_downloads >= MAX_DOWNLOADS_FREE: print("\n[bold red]✘ Batas download gratis telah tercapai![/bold red]") print("[bold cyan]Dapatkan lisensi: https://wa.me/6287825946251[/bold cyan]\n") input("Tekan Enter untuk kembali...") else: url = Prompt.ask("Masukkan URL Media") download_media(url) if not is_developer: user_downloads += 1 elif pilihan == "2": print(f"\nFolder penyimpanan media: [green]{DOWNLOAD_FOLDER}[/green]\n") elif pilihan == "3": print("\n[bold blue]Developer: bzonedev87[/bold blue]") print("GitHub: https://github.com/bzdev87") print("WhatsApp: https://wa.me/6287825946251\n") elif pilihan == "4": print("\n[bold yellow]Masukkan URL dari Instagram, TikTok, dll dan media akan diunduh ke folder bzdownloader.[/bold yellow]\n") elif pilihan == "5" and is_developer: print("\n[bold green]>>> Developer Mode aktif! <<<[/bold green]\n") os.system("ls -la") elif pilihan in ["5", "6"]: print("\n[bold cyan]Keluar...[/bold cyan]") sys.exit()

input("\nTekan Enter untuk kembali ke menu...")
show_banner()
main_menu(is_developer)

Fungsi download

def download_media(url): print("\n[cyan]Mendownload...[/cyan]\n") with Progress() as progress: task = progress.add_task("[green]Mengunduh...", total=100) os.system(f"yt-dlp -o '{DOWNLOAD_FOLDER}/%(title)s.%(ext)s' {url}") progress.update(task, completed=100) print("\n[bold green]Selesai![/bold green]\n")

Eksekusi

if name == "main": show_banner() dev_mode = check_license() main_menu(dev_mode)

