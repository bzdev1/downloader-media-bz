#!/usr/bin/env python3

bzdev87 - Social Media Downloader (All-in-One)

import os import sys import time import socket from datetime import datetime from pathlib import Path

try: from yt_dlp import YoutubeDL except ImportError: print("\n[!] Modul 'yt_dlp' belum terpasang. Menginstal...") os.system("pip install yt-dlp") from yt_dlp import YoutubeDL

Konfigurasi Awal

DOWNLOAD_DIR = str(Path.home()) + "/bzdownloader" LICENSE_FILE = "licenses.txt" LOG_FILE = "users_log.txt" DEVELOPER_WA = "+62 878-2594-6251"

Lisensi Valid (hanya contoh, kamu bisa tambah di licenses.txt)

def load_valid_licenses(): if not os.path.exists(LICENSE_FILE): open(LICENSE_FILE, 'w').close() with open(LICENSE_FILE, 'r') as f: return [x.strip() for x in f.readlines() if x.strip() != '']

def log_user(license_key): ip = socket.gethostbyname(socket.gethostname()) user = os.getenv("USER") or os.getenv("USERNAME") or "UnknownUser" now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") with open(LOG_FILE, 'a') as f: f.write(f"[{now}] Nama: {user} | Lisensi: {license_key} | IP: {ip}\n")

def cek_lisensi(): print("\n[ Lisensi Diperlukan untuk Mengakses Script Ini ]") lisensi = input("Masukkan Lisensi Anda: ").strip() valid = load_valid_licenses() if lisensi in valid: log_user(lisensi) return True else: print(f"\n[!] Lisensi tidak valid atau kadaluarsa!") print(f"[!] Hubungi WA untuk lisensi baru: {DEVELOPER_WA}\n") return False

def show_banner(): os.system('clear') print(""" ╭────────────────────────────────────────────────────────────────────╮ │                                                                    │ │ ██████  ███████ ███████ ██████  ███████ ██    ██ ███████ ██    ██  │ │ ██   ██ ██      ██      ██   ██ ██       ██  ██  ██       ██  ██   │ │ ██   ██ █████   █████   ██████  █████     ████   █████     ████    │ │ ██   ██ ██      ██      ██      ██         ██    ██         ██     │ │ ██████  ███████ ███████ ██      ███████    ██    ███████    ██     │ │                                                                    │ │ >>> bzdev87 Social Media Downloader - All in One <<<               │ ╰────────────────────────────────────────────────────────────────────╯ """)

def menu(): while True: print(""" MENU UTAMA ┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ┃ No ┃ Aksi                           ┃ ┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩ │ 1  │ Download Media Sosial         │ │ 2  │ Buka Folder Download          │ │ 3  │ Info Developer                │ │ 4  │ Bantuan / Cara Pakai          │ │ 5  │ Menu Khusus Developer         │ │ 6  │ Keluar                        │ └────┴────────────────────────────────┘ ") pilihan = input("Masukkan pilihan [1-6]: ").strip() if pilihan == '1': url = input("Masukkan URL Media: ").strip() download_media(url) elif pilihan == '2': print(f"\nFolder penyimpanan: {DOWNLOAD_DIR}\n") elif pilihan == '3': print("\nDeveloper: bzdev87 (https://github.com/bzdev87)") print(f"Kontak WhatsApp: {DEVELOPER_WA}\n") elif pilihan == '4': print("\n[!] Cukup masukkan URL video/foto dari TikTok, IG, Facebook, dll.") print("Hasil akan otomatis tersimpan di folder bzdownloader.\n") elif pilihan == '5': show_developer_log() elif pilihan == '6': print("\nTerima kasih telah menggunakan bzdev87!") sys.exit() else: print("\n[!] Pilihan tidak valid.")

def show_developer_log(): if os.path.exists(LOG_FILE): print("\n[ Log Pengguna Aktif: ]\n") with open(LOG_FILE, 'r') as f: print(f.read()) else: print("\n[!] Belum ada pengguna terdaftar.\n")

def download_media(url): print("\nMendownload...\n") ydl_opts = { 'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s', 'quiet': False } try: with YoutubeDL(ydl_opts) as ydl: ydl.download([url]) except Exception as e: print(f"Gagal download: {e}")

def prepare_folder(): if not os.path.exists(DOWNLOAD_DIR): os.makedirs(DOWNLOAD_DIR) print(f"\nFolder dibuat: {DOWNLOAD_DIR}")

if name == 'main': prepare_folder() show_banner() if cek_lisensi(): menu()

