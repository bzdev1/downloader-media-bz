import os import time import sys import subprocess

Lokasi file lisensi rahasia

LICENSE_FILE = ".data_lc87.txt" VALID_LICENSES = []

Baca lisensi dari file tersembunyi

if os.path.exists(LICENSE_FILE): with open(LICENSE_FILE, "r") as f: VALID_LICENSES = [line.strip() for line in f if line.strip() and not line.startswith("#")] else: with open(LICENSE_FILE, "w") as f: f.write("# Valid Licenses\nDEV-BZ87-2025-ALFA\nPUB-ACCESS-2025\n") VALID_LICENSES = ["DEV-BZ87-2025-ALFA", "PUB-ACCESS-2025"]

Fungsi clear

clear = lambda: os.system("clear")

Cek folder download

download_folder = os.path.expanduser("~/bzdownloader") os.makedirs(download_folder, exist_ok=True)

Fungsi tampilan

def banner(): print(""" ╭────────────────────────────────────────────────────────────────────╮ │                                                                    │ │ ██████  ███████ ███████ ██████  ███████ ██    ██ ███████ ██    ██  │ │ ██   ██ ██      ██      ██   ██ ██       ██  ██  ██       ██  ██   │ │ ██   ██ █████   █████   ██████  █████     ████   █████     ████    │ │ ██   ██ ██      ██      ██      ██         ██    ██         ██     │ │ ██████  ███████ ███████ ██      ███████    ██    ███████    ██     │ │                                                                    │ │ >>> bzdev87 Social Media Downloader - All in One <<<               │ ╰────────────────────────────────────────────────────────────────────╯""")

Fungsi lisensi

def cek_lisensi(): clear() print("[!] Lisensi diperlukan untuk menggunakan tool ini.") lisensi = input("Masukkan lisensi Anda: ").strip() if lisensi in VALID_LICENSES: if lisensi.startswith("DEV-"): print("[+] Lisensi Developer valid. Akses penuh diberikan.") else: print("[+] Lisensi valid. Akses publik diberikan.") time.sleep(1) else: print("[X] Lisensi tidak valid!") print("Silakan hubungi Admin untuk mendapatkan lisensi:") print("WhatsApp: +62 878-2594-6251") sys.exit()

Menu utama

def menu(): while True: clear() banner() print(""" MENU UTAMA ┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓ ┃ No ┃ Aksi                 ┃ ┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩ │ 1  │ Download Media       │ │ 2  │ Buka Folder Download │ │ 3  │ Info Developer       │ │ 4  │ Bantuan / Cara Pakai │ │ 5  │ Keluar               │ └────┴──────────────────────┘""") pilihan = input("Masukkan pilihan [1/2/3/4/5]: ").strip() if pilihan == "1": url = input("Masukkan URL Media: ").strip() print("\n⠏ Mendownload...") cmd = f"yt-dlp -o '{download_folder}/%(title)s.%(ext)s' {url}" os.system(cmd) input("\n[✓] Tekan ENTER untuk kembali ke menu...") elif pilihan == "2": print(f"\nFolder penyimpanan media:\n{download_folder}") input("\n[✓] Tekan ENTER untuk kembali ke menu...") elif pilihan == "3": print("\nDeveloper: @bzdev87") print("GitHub   : https://github.com/bzdev87") input("\n[✓] Tekan ENTER untuk kembali ke menu...") elif pilihan == "4": print(""" Cara Pakai:

1. Pilih menu 1 lalu masukkan URL video atau media.


2. Hasil download otomatis tersimpan ke folder bzdownloader.


3. Jika lisensi invalid, hubungi +62 878-2594-6251. """) input("\n[✓] Tekan ENTER untuk kembali ke menu...") elif pilihan == "5": print("\n[!] Keluar...") time.sleep(1) break else: print("[!] Pilihan tidak valid.") time.sleep(1)



Eksekusi awal

if name == "main": cek_lisensi() menu()

