#!/usr/bin/env python3
import os
import sys
import yt_dlp
import time
import platform
import requests
from urllib.parse import urlparse
from termcolor import cprint

def banner():
    os.system("clear")
    cprint("""
 ██████╗ ███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗
 ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝╚██╗ ██╔╝
 ██████╔╝█████╗  ██║   ██║██║  ██║█████╗   ╚████╔╝ 
 ██╔═══╝ ██╔══╝  ██║   ██║██║  ██║██╔══╝    ╚██╔╝  
 ██║     ███████╗╚██████╔╝██████╔╝███████╗   ██║   
 ╚═╝     ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝   
    """, "cyan")
    cprint("Developer License aktif - akses penuh", "green", attrs=["bold"])

def buat_lisensi():
    print("\nFitur ini sedang dalam pengembangan...\n")

def tentang_aplikasi():
    cprint("\nDownloader-Media-BZ", "yellow")
    print("Versi: 2.0 - Pro Edition")
    print("Developer: BzDev87")
    print("Support: YouTube, Facebook, TikTok, Instagram, X/Twitter, dll")
    print("Library: yt-dlp")
    print("Lisensi: Open Source\n")

def download_media():
    urls = input("Masukkan URL media (pisahkan dengan koma untuk banyak): ").split(',')
    jenis = input("Pilih jenis media [Video/MP3/Gambar/Semua]: ").strip().lower()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        output_dir = "/sdcard/Download" if platform.system() == "Linux" else "downloads"
        ydl_opts = {
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'merge_output_format': 'mp4',
        }

        if jenis == 'mp3':
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            })
        elif jenis == 'gambar':
            try:
                response = requests.get(url)
                fname = os.path.basename(urlparse(url).path)
                if not fname:
                    fname = f'gambar_{int(time.time())}.jpg'
                path = os.path.join(output_dir, fname)
                with open(path, 'wb') as f:
                    f.write(response.content)
                print(f'Selesai download gambar: {path}')
                continue
            except Exception as e:
                print(f'Gagal download gambar: {e}')
                continue
        elif jenis in ['semua', 'video']:
            ydl_opts['format'] = 'bestvideo+bestaudio/best'

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                print(f"Selesai: {info.get('title', 'Video berhasil diunduh')}")
        except yt_dlp.utils.DownloadError as e:
            print(f"Gagal download: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def main_menu():
    while True:
        banner()
        print("""
 MENU UTAMA
 ┏━━━━┳━━━━━━━━━━━━━━━━━━━┓
 ┃ No ┃ Aksi              ┃
 ┡━━━━╇━━━━━━━━━━━━━━━━━━━┩
 │ 1  │ Download Media    │
 │ 2  │ Buat Lisensi Baru │
 │ 3  │ Tentang Aplikasi  │
 │ 4  │ Keluar            │
 └────┴───────────────────┘
        """)
        pilihan = input("Pilih opsi [1/2/3/4]: ").strip()

        if pilihan == '1':
            download_media()
        elif pilihan == '2':
            buat_lisensi()
        elif pilihan == '3':
            tentang_aplikasi()
        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan Downloader-Media-BZ!")
            sys.exit(0)
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == '__main__':
    main_menu()
