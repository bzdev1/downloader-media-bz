import os, sys, requests from rich.console import Console from rich.prompt import Prompt from rich.table import Table from rich.progress import Progress import yt_dlp

console = Console() LICENSE_FILE = "license.txt" DOWNLOAD_FOLDER = "/sdcard/Download" WHATSAPP_CONTACT = "https://wa.me/6287825946251"

def show_banner(): banner = """ [bold magenta] ██████╗ ███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗ ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝╚██╗ ██╔╝ ██████╔╝█████╗  ██║   ██║██║  ██║█████╗   ╚████╔╝ ██╔═══╝ ██╔══╝  ██║   ██║██║  ██║██╔══╝    ╚██╔╝
██║     ███████╗╚██████╔╝██████╔╝███████╗   ██║
╚═╝     ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝
[/bold magenta]
""" console.print(banner)

def update_yt_dlp(): try: console.print("[yellow]Memeriksa pembaruan yt-dlp...[/yellow]") os.system("pip install -U yt-dlp > /dev/null") console.print("[green]yt-dlp berhasil diperbarui![/green]") except Exception as e: console.print(f"[red]Gagal update yt-dlp:[/red] {e}")

def create_download_folder(): if not os.path.exists(DOWNLOAD_FOLDER): os.makedirs(DOWNLOAD_FOLDER)

def create_license(jenis): with open(LICENSE_FILE, "w") as f: f.write(f"LICENSE_TYPE={jenis}\n") console.print(f"[bold green]Lisensi {jenis} berhasil dibuat![/bold green]")

def hook(d): if d['status'] == 'finished': console.print(f"[bold green]Selesai:[/bold green] {d['filename']}")

def is_valid_url(url): return url.startswith("http://") or url.startswith("https://")

def download_media(urls, mode): create_download_folder() if isinstance(urls, str): urls = [urls]

for url in urls:
    if not is_valid_url(url):
        console.print(f"[red]URL tidak valid:[/red] {url}")
        continue

    output = os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s')

    if mode == "Video":
        ydl_opts = {
            'outtmpl': output,
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'progress_hooks': [hook],
            'allow_unplayable_formats': True,
            'force_generic_extractor': False,
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
            'allow_unplayable_formats': True,
            'force_generic_extractor': False,
        }
    elif mode == "Gambar":
        try:
            r = requests.get(url)
            filename = os.path.join(DOWNLOAD_FOLDER, url.split("/")[-1])
            with open(filename, "wb") as f:
                f.write(r.content)
            console.print(f"[bold green]Gambar disimpan ke:[/bold green] {filename}")
        except Exception as e:
            console.print(f"[bold red]Gagal download gambar:[/bold red] {e}")
        continue
    elif mode == "Semua":
        for tipe in ["Video", "MP3", "Gambar"]:
            download_media([url], tipe)
        continue
    else:
        console.print("[red]Mode tidak dikenal.[/red]")
        return

    try:
        with Progress() as progress:
            task = progress.add_task("[cyan]Mendownload...", total=None)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            progress.update(task, completed=100)
    except yt_dlp.utils.DownloadError:
        console.print(f"[red]Format tidak ditemukan, mencoba fallback format...[/red]")
        try:
            ydl_opts['format'] = 'best'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            console.print(f"[bold red]Gagal download ulang:[/bold red] {e}")
    except yt_dlp.utils.UnsupportedError:
        console.print(f"[red]Situs tidak didukung: {url}[/red]")
    except Exception as e:
        console.print(f"[bold red]Terjadi kesalahan saat mendownload:[/bold red] {e}")

def menu(): table = Table(title="[bold cyan]MENU UTAMA[/bold cyan]", show_header=True, header_style="bold magenta") table.add_column("No", style="bold yellow") table.add_column("Aksi", style="bold white") table.add_row("1", "Download Media") table.add_row("2", "Buat Lisensi Baru") table.add_row("3", "Tentang Aplikasi") table.add_row("4", "Keluar") console.print(table)

def check_license(): if not os.path.exists(LICENSE_FILE): console.print("[bold red]Lisensi tidak ditemukan![/bold red]") open_license = Prompt.ask("Ingin aktivasi lisensi sekarang? (y/n)", choices=["y", "n"]) if open_license == "y": os.system(f"termux-open-url {WHATSAPP_CONTACT}") sys.exit()

with open(LICENSE_FILE, "r") as f:
    content = f.read()
    if "LICENSE_TYPE=developer" in content:
        console.print("[bold cyan]Developer License aktif - akses penuh[/bold cyan]")
    elif "LICENSE_TYPE=Publik" in content:
        console.print("[bold green]Lisensi Publik aktif[/bold green]")
    else:
        console.print("[bold red]Format lisensi tidak valid.[/bold red]")
        sys.exit()

def run(): show_banner() update_yt_dlp() check_license() create_download_folder()

while True:
    menu()
    pilihan = Prompt.ask("[bold yellow]Pilih opsi[/bold yellow]", choices=["1", "2", "3", "4"])

    if pilihan == "1":
        url_input = Prompt.ask("[cyan]Masukkan URL media (pisahkan dengan koma untuk banyak)[/cyan]")
        url_list = [u.strip() for u in url_input.split(",")]
        mode = Prompt.ask("Pilih jenis media", choices=["Video", "MP3", "Gambar", "Semua"])
        download_media(url_list, mode)
    elif pilihan == "2":
        jenis = Prompt.ask("Jenis lisensi (Publik/Developer)", choices=["Publik", "Developer"])
        create_license(jenis)
    elif pilihan == "3":
        console.print("[bold cyan]Aplikasi ini dibuat oleh BZDev87. Lisensi terbatas.[/bold cyan]")
    elif pilihan == "4":
        console.print("[bold magenta]Sampai jumpa![/bold magenta]")
        break

if name == "main": run()

