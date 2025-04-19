from rich.console import Console from rich.prompt import Prompt from rich.panel import Panel import yt_dlp import requests import os

console = Console()

def auth(): akun = {"bzdev87": "1sampai1"} console.print("[bold cyan]Login diperlukan[/bold cyan]") username = Prompt.ask("Username") password = Prompt.ask("Password", password=True) if username in akun and akun[username] == password: console.print(f"[green]Login berhasil sebagai {username}[/green]") return True else: console.print("[red]Login gagal. Coba lagi.[/red]") return False

def download_media(url_list, mode): for u in url_list: try: if mode == "Video": opts = { 'outtmpl': 'video_%(id)s.%(ext)s', 'format': 'bestvideo+bestaudio/best', 'merge_output_format': 'mp4', } console.print(f"[blue]Mengunduh video dari {u}[/blue]") with yt_dlp.YoutubeDL(opts) as ydl: ydl.download([u])

elif mode == "MP3":
            opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'audio_%(id)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            console.print(f"[blue]Mengunduh MP3 dari {u}[/blue]")
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([u])

        elif mode == "Gambar":
            r = requests.get(u, stream=True)
            if r.status_code == 200:
                fname = "img_" + u.split("/")[-1].split("?")[0][:40]
                with open(fname, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                console.print(f"[green]Gambar tersimpan sebagai {fname}[/green]")
            else:
                console.print("[red]Gagal unduh gambar[/red]")

        elif mode == "Semua":
            console.print(f"[blue]Mengunduh semua dari {u}[/blue]")
            # Video
            opts_vid = {
                'outtmpl': 'video_%(id)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
            }
            with yt_dlp.YoutubeDL(opts_vid) as ydl:
                ydl.download([u])
            # MP3
            opts_mp3 = {
                'format': 'bestaudio/best',
                'outtmpl': 'audio_%(id)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(opts_mp3) as ydl:
                ydl.download([u])

        console.print("[green]Selesai[/green]")

    except Exception as e:
        console.print(f"[red]Gagal download: {e}[/red]")

def run(): if not auth(): return

while True:
    console.print(Panel("""

██████╗ ███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗ ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝╚██╗ ██╔╝ ██████╔╝█████╗  ██║   ██║██║  ██║█████╗   ╚████╔╝ ██╔═══╝ ██╔══╝  ██║   ██║██║  ██║██╔══╝    ╚██╔╝
██║     ███████╗╚██████╔╝██████╔╝███████╗   ██║
╚═╝     ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝
""", title="downloader-bz"))

console.print("""
    MENU UTAMA

┏━━━━┳━━━━━━━━━━━━━━━━━━━┓ ┃ No ┃ Aksi              ┃ ┡━━━━╇━━━━━━━━━━━━━━━━━━━┩ │ 1  │ Download Media    │ │ 2  │ Tentang Aplikasi  │ │ 3  │ Keluar            │ └────┴───────────────────┘ """)

pilihan = Prompt.ask("Pilih opsi", choices=["1", "2", "3"])

    if pilihan == "1":
        url_input = Prompt.ask("[cyan]Masukkan URL media (pisahkan dengan koma untuk banyak)[/cyan]")
        url_list = [u.strip() for u in url_input.split(",")]
        mode = Prompt.ask("Pilih jenis media", choices=["Video", "MP3", "Gambar", "Semua"])
        download_media(url_list, mode)
    elif pilihan == "2":
        console.print("[bold cyan]Aplikasi ini dibuat oleh BZDev87. Lisensi terbatas.[/bold cyan]")
    elif pilihan == "3":
        console.print("[bold magenta]Sampai jumpa![/bold magenta]")
        break

if name == "main": run()

