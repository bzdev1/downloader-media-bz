import os
import time
import sys
import subprocess

Lokasi file lisensi dan log

LICENSE_FILE = "licenses.txt" LOG_FILE = "users_log.txt" DATA_FILE = ".data_lc87.txt"

Lisensi valid (RAHASIA)

VALID_LICENSES = [ "LC87-X2VZ-9021-HIDENKEY", "LC87-PUB-2025-DEMO" ]

Batasan lisensi publik

LIMIT_PUB = 3

Fungsi validasi lisensi

def validasi_lisensi(): if not os.path.exists(LICENSE_FILE): print("[!] File lisensi tidak ditemukan.") return False with open(LICENSE_FILE) as f: license_key = f.read().strip() if license_key in VALID_LICENSES: if license_key == "LC87-PUB-2025-DEMO": return "PUB" return True return False

Fungsi untuk mencatat pengguna yang mengakses

def log_pengguna(): user = os.getenv("USER") or os.getenv("USERNAME") or "unknown" with open(LOG_FILE, "a") as f: f.write(f"{user} | {time.ctime()}\n")

Menu utama def

def menu(): os.system("clear") print(""" ╭────────────────────────────────────────────────────────────────────╮ │                                                                    │ │ ██████  ███████ ███████ ██████  ███████ ██    ██ ███████ ██    ██  │ │ ██   ██ ██      ██      ██   ██ ██       ██  ██  ██       ██  ██   │ │ ██   ██ █████   █████   ██████  █████     ████   █████     ████    │ │ ██   ██ ██      ██      ██      ██         ██    ██         ██     │ │ ██████  ███████ ███████ ██      ███████    ██    ███████    ██     │ │                                                                    │ │ >>> bzdev87 Social Media Downloader - All in One <<<               │ ╰────────────────────────────────────────────────────────────────────╯ """) print(""" MENU UTAMA ┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ┃ No ┃ Aksi                              ┃ ┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩ │ 1  │ Download Media Sosial             │ │ 2  │ Buka Folder Download              │ │ 3  │ Info Developer                    │ │ 4  │ Bantuan / Cara Pakai              │ │ 5  │ Developer Mode (Lisensi Khusus)   │ │ 6  │ Keluar                            │ └────┴───────────────────────────────────┘ """) return input("Masukkan pilihan [1/2/3/4/5/6]: ")

Developer khusus

def developer_mode(): print("\n[+] Developer Mode AKTIF") print("[+] Lisensi: TERDAFTAR") print("[+] WA Developer: wa.me/6287825946251") print("[+] Daftar pengguna tersimpan di:", LOG_FILE) print("\n[+] Fitur:") print(" - Monitor Pengguna") print(" - Export data lisensi") print(" - Reset Batas Publik")

Fungsi utama

if name == "main": status = validasi_lisensi()

if status == False:
    print("[!] Lisensi tidak valid.")
    print("[!] Hubungi WA untuk akses: wa.me/6287825946251")
    sys.exit()
elif status == "PUB":
    # Batas publik
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            f.write("1")
    else:
        with open(DATA_FILE) as f:
            count = int(f.read().strip())
        if count >= LIMIT_PUB:
            print("[!] Batas penggunaan publik tercapai.")
            print("[!] Upgrade lisensi ke full access: wa.me/6287825946251")
            sys.exit()
        else:
            with open(DATA_FILE, "w") as f:
                f.write(str(count + 1))

log_pengguna()

while True:
    pilihan = menu()
    if pilihan == "1":
        print("[>] Fitur download akan ditambahkan.")
    elif pilihan == "2":
        print("[>] Buka folder download...")
        os.system("xdg-open bzdownloader")
    elif pilihan == "3":
        print("[>] Developer: github.com/bzdev87")
    elif pilihan == "4":
        print("[>] Cara pakai: Masukkan link media dari IG, TikTok, dll")
    elif pilihan == "5":
        developer_mode()
    elif pilihan == "6":
        print("[!] Keluar...")
        break
    else:
        print("[!] Pilihan tidak valid.")
    input("\nTekan ENTER untuk kembali ke menu...")

