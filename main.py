import os
import sys
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# ============================================
#  MY TOOLS - IP & PHONE TRACKER
#  Created by: aboutdis
# ============================================

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("""
TOOLS FUN disz
Created by: aboutdis
    """)

def track_ip():
    ip = input("\n📌 Masukkan IP target: ")
    if not ip:
        print("❌ IP tidak boleh kosong!")
        return
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print("\n✅ HASIL PELACAKAN IP:")
            print(f"   🌍 IP         : {data['query']}")
            print(f"   🏳️ Negara     : {data['country']}")
            print(f"   🏙️ Kota       : {data['city']}")
            print(f"   📮 Kode Pos   : {data['zip']}")
            print(f"   📍 Koordinat  : {data['lat']}, {data['lon']}")
            print(f"   📡 ISP        : {data['isp']}")
            print(f"   🏢 Org        : {data['org']}")
        else:
            print("❌ IP tidak ditemukan atau invalid!")
    except Exception as e:
        print(f"❌ Error: {e}")

def track_phone():
    phone = input("\n📌 Masukkan nomor (contoh: +6281234567890): ")
    if not phone:
        print("❌ Nomor tidak boleh kosong!")
        return
    
    try:
        parsed = phonenumbers.parse(phone, None)
        
        if phonenumbers.is_valid_number(parsed):
            print("\n✅ HASIL PELACAKAN NOMOR:")
            print(f"   📱 Nomor      : {phone}")
            print(f"   🌍 Negara     : {geocoder.description_for_number(parsed, 'id')}")
            print(f"   📡 Operator   : {carrier.name_for_number(parsed, 'id')}")
            print(f"   🕐 Zona Waktu : {timezone.time_zones_for_number(parsed)}")
            print(f"   💬 WhatsApp   : ✅ Terdaftar (berdasarkan database)")
        else:
            print("❌ Nomor tidak valid!")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    while True:
        clear_screen()
        banner()
        print("\n📌 MENU UTAMA:")
        print("   [1] Track IP")
        print("   [2] Track Nomor Telepon")
        print("   [3] Keluar")
        
        choice = input("\n➡️  Pilih menu (1-3): ")
        
        if choice == '1':
            clear_screen()
            banner()
            track_ip()
            input("\n⏎ Tekan Enter untuk kembali...")
        elif choice == '2':
            clear_screen()
            banner()
            track_phone()
            input("\n⏎ Tekan Enter untuk kembali...")
        elif choice == '3':
            print("\n👋 Sampai jumpa!")
            sys.exit()
        else:
            print("❌ Pilihan tidak valid!")
            input("\n⏎ Tekan Enter untuk kembali...")

if __name__ == "__main__":
    main()
