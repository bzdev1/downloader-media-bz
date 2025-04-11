# install.sh
#!/data/data/com.termux/files/usr/bin/bash

echo "Menginstal dependensi..."
pkg update -y
pkg install python git -y
pip install -r requirements.txt

echo "Instalasi selesai!"
