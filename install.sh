import os import sys import time import subprocess from rich import print from rich.console import Console from rich.table import Table

Konfigurasi

DOWNLOAD_DIR = "/sdcard/bzdownloader" LICENSE_KEY = "DEV-BZ87-2025-FULLACCESS" MAX_FREE_DOWNLOADS = 3

console = Console() download_count = 0 developer_mode = False

Fungsi

def check_license(): global developer_mode os.system("clear") console.print("[cyan]Cek Lisensi Developer...[/cyan]") try: with open("license.key", "r") as f: for line in f: if line.strip().endswith(LICENSE_KEY): developer_mode = True console.print("[green]Akses Developer Aktif![/green]") return except: pass

console.print("[yellow]Tidak ada lisensi. Akses dibatasi.[/yellow]")
console.print("[bold red]Hubungi WhatsApp: +62 878-2594-6251 untuk lisensi.[/bold red]")
time.sleep(3)

def tampil_banner(): os.system("clear") console.print(""" [bold cyan] ╭────────────────────────────────────────────────────────────────────╮ │                                                                    │ │ ██████  ███████ ███████ ██████  ███████ ██   ██ ███████ ██   ██    │ │ ██   ██ ██      ██      ██   ██ ██       ██ ██  ██       ██ ██     │ │ ██   ██ █████   █████   ██████  █████     ███   █████     ███      │ │ ██   ██ ██      ██      ██   ██ ██       ██ ██  ██       ██ ██     │ │ ██████  ███████ ███████ ██   ██ ███████ ██   ██ ███████ ██   ██    │ │                                                                    │ │ >>> bzdev87 Social Media Downloader - All in One <<<               │ ╰────────────────────────────────────────────────────────────────────╯ [/bold cyan]""")

def buat_folder(): if not os.path.exists(DOWNLOAD_DIR): os.makedirs(DOWNLOAD_DIR)

def menu(): table = Table(show_header=True, header_style="bold magenta") table.add_column("No", style="dim", width=6) table.add_column("Aksi") table.add_row("1", "Download Media") table.add_row("2", "Buka Folder Download") table.add_row("3", "Info Developer") table.add_row("4", "Bantuan / Cara Pakai") if developer_mode: table.add_row("5", "Menu Developer") table.add_row("0", "Keluar") console.print(table)

def download_media(): global download_count if not developer_mode and download_count >= MAX_FREE_DOWNLOADS: console.print("[red]Limit download gratis tercapai.[/red]") console.print("[yellow]Minta lisensi ke WhatsApp: +62 878-2594-6251[/yellow]") return

url = console.input("[bold cyan]Masukkan URL Media: [/bold cyan]")
if url:
    console.print("[green]Mendownload...[/green]")
    try:
        subprocess.run(["yt-dlp", url, "-o", f"{DOWNLOAD_DIR}/%(title)s.%(ext)s"])
        download_count += 1
        console.print(f"[green]Selesai. File tersimpan di {DOWNLOAD_DIR}[/green]")
    except Exception as e:
        console.print(f"[red]Gagal: {e}[/red]")

def buka_folder(): console.print(f"[blue]Folder penyimpanan: {DOWNLOAD_DIR}[/blue]") os.system(f"termux-open {DOWNLOAD_DIR}")

def info_dev(): console.print("[bold green]Developer: bzdev87[/bold green]") console.print("[yellow]WA: +62 878-2594-6251[/yellow]") console.print("GitHub: [link=https://github.com/bzdev87]github.com/bzdev87[/link]")

def bantuan(): console.print(""" [cyan]Cara Pakai:

1. Pilih menu Download Media


2. Masukkan link dari TikTok, IG, dll


3. File otomatis tersimpan ke /sdcard/bzdownloader [/cyan] """)



def menu_dev(): console.print("[bold magenta]:: Menu Developer ::[/bold magenta]") console.print("- Mode ini hanya untuk pemilik lisensi resmi") console.print("- Fitur tambahan akan tersedia di versi berikutnya")

def main(): check_license() buat_folder() while True: tampil_banner() menu() pilihan = console.input("[bold cyan]Masukkan pilihan [0-5]: [/bold cyan]") if pilihan == "1": download_media() elif pilihan == "2": buka_folder() elif pilihan == "3": info_dev() elif pilihan == "4": bantuan() elif pilihan == "5" and developer_mode: menu_dev() elif pilihan == "0": break else: console.print("[red]Pilihan tidak valid[/red]") input("[bold blue]\nTekan Enter untuk kembali ke menu...[/bold blue]")

if name == "main": main()

