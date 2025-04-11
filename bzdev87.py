import os import sys import subprocess from rich.console import Console from rich.prompt import Prompt from rich.table import Table from rich.progress import Progress import yt_dlp

console = Console() DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads") os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def hook(d): if d['status'] == 'finished': console.print("\n[bold green]Download selesai, memproses video...[/bold green]")

def download_video(url, auto_fix=True): ydl_opts = { 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 'merge_output_format': 'mp4', 'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title).80s.%(ext)s'), 'postprocessors': [{ 'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4' }], 'postprocessor_args': ['-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental'], 'noplaylist': True, 'progress_hooks': [hook], }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        result = ydl.download([url])
    except Exception as e:
        console.print(f"[red]Error saat download: {e}[/red]")
        return

if auto_fix:
    fix_video_compatibility()

def fix_video_compatibility(): for file in os.listdir(DOWNLOAD_FOLDER): if file.endswith(".mp4"): input_path = os.path.join(DOWNLOAD_FOLDER, file) output_path = os.path.join(DOWNLOAD_FOLDER, f"fixed_{file}") command = [ "ffmpeg", "-i", input_path, "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", output_path ] try: subprocess.run(command, check=True) os.remove(input_path) os.rename(output_path, input_path) console.print(f"[green]Video fixed: {file}[/green]") except subprocess.CalledProcessError: console.print(f"[red]Gagal memperbaiki file: {file}[/red]")

def main(): console.print("[bold cyan]=== Downloader Media BZ ===[/bold cyan]") url = Prompt.ask("Masukkan URL video") download_video(url, auto_fix=True)

if name == 'main': main()

