import os
import time
import subprocess

DOWNLOAD_FOLDER = "/data/data/com.termux/files/home/bzdownloader"
VALID_LICENSE_FILE = "valid_licenses.txt"
LICENSE_KEY_FILE = "license_key.txt"
WA_CONTACT = "+62 878-2594-6251"

def clear():
    os.system("clear")

def banner():
    print("╭" + "─" * 68 + "╮")
    print("│" + " " * 68 + "│")
    print("│  ██████  ███████ ███████ ██████  ███████ ██    ██ ███████ ██    ██  │")
    print("│  ██   ██ ██      ██      ██   ██ ██       ██  ██  ██       ██  ██   │")
    print("│  ██   ██ █████   █████   ██████  █████     ████   █████     ████    │")
    print("│  ██   ██ ██      ██      ██      ██         ██    ██         ██     │")
    print("│  ██████  ███████ ███████ ██      ███████    ██    ███████    ██     │")
    print("│                                                                    │")
    print(f"│ >>> bzdev87 Social Media Downloader - All in One <<<               │")
    print("╰" + "─" * 68 + "╯")

def check_license():
    if not os.path.exists(LICENSE_KEY_FILE):
        print("\n[!] Lisensi belum ditemukan.")
        input_key = input("Masukkan lisensi anda: ").strip()
        if validate_license(input_key):
            with open(LICENSE_KEY_FILE, "w") as f:
                f.write(input_key)
            print("[✓] Lisensi valid! Akses penuh diberikan.")
            time.sleep(1)
        else:
            print("\n[x] Lisensi tidak valid.")
            print(f"[!] Hubungi WA untuk dapatkan lisensi: {WA_CONTACT}")
            exit()
    else:
        with open(LICENSE_KEY_FILE, "r") as f:
            license_key = f.read().strip()
            if not validate_license(license_key):
                print("\n[x] Lisensi tidak valid atau kadaluarsa.")
                print(f"[!] Hubungi WA: {WA_CONTACT}")
                exit()

def validate_license(key):
    if not os.path.exists(VALID_LICENSE_FILE):
        return False
    with open(VALID_LICENSE_FILE, "r") as f:
        return key in [line.strip() for line in f.readlines()]

def create_download_folder():
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
        print(f"Folder dibuat: {DOWNLOAD_FOLDER}")

def main_menu():
    while True:
        print("\n         MENU UTAMA")
        print("┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃ No ┃ Aksi                 ┃")
        print("┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩")
        print("│ 1  │ Download Media       │")
        print("│ 2  │ Buka Folder Download │")
        print("│ 3  │ Info Developer       │")
        print("│ 4  │ Bantuan / Cara Pakai │")
        print("│ 5  │ Keluar               │")
        print("└────┴──────────────────────┘")

        pilihan = input("Masukkan pilihan [1/2/3/4/5]: ").strip()
        if pilihan == "1":
            url = input("Masukkan URL Media: ").strip()
            download_media(url)
        elif pilihan == "2":
            print(f"\nFolder penyimpanan media:\n{DOWNLOAD_FOLDER}")
        elif pilihan == "3":
            print(f"\nDeveloper: BzDev87\nGitHub: https://github.com/bzdev87")
        elif pilihan == "4":
            print("\n1. Salin link media dari TikTok, IG, YouTube, dll.")
            print("2. Masukkan ke menu [1]")
            print("3. File akan otomatis tersimpan di folder bzdownloader")
        elif pilihan == "5":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak tersedia!")

def download_media(url):
    print("⠏ Mendownload...")
    try:
        subprocess.run(
            ["yt-dlp", "-o", f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s", url],
            check=True
        )
        print("[✓] Download selesai!")
    except subprocess.CalledProcessError:
        print("[x] Gagal download: URL tidak didukung atau kesalahan lainnya.")

if __name__ == "__main__":
    clear()
    banner()
    check_license()
    create_download_folder()
    main_menu()
