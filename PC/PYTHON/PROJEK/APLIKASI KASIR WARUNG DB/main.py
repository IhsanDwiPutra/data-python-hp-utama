import os
import random

# Fungsi untuk membuat ID random dengan 3 digit angka
def buatIDAngka():
    id_random = ''.join(random.choice('0123456789') for _ in range(3))
    return id_random

# Fungsi clear screen / membersihkan layar
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan pesan di tengah dengan garis
def tengahGaris(pesan):
    print(pesan.center(60,'-'))

# List untuk menyimpan data kasir
daftar_kasir = []

# Fungsi untuk menampilkan daftar kasir
def lihatDaftarKasir():
    clearScreen()
    if daftar_kasir:
        print((5*'-'+" DAFTAR KASIR YANG TERDAFTAR "+5*'-').center(60,' ')) 
        
        # no id nama, umur, alamat, no wa
        # [id, nama_kasir, umur_kasir, alamat_kasir, no_wa]
        print('\n')
        print(60*'-')
        print("| NO | ID | NAMA       | UMUR | ALAMAT     | NO WA         |")
        print(60*'-')
        for index, kasir in enumerate(daftar_kasir, start=1):
            print(f"| {index:<3}| {kasir[0]:<3}| {kasir[1]:<11}| {kasir[2]:^5}| {kasir[3]:<11}| 0{kasir[4]:<13}|")
    else:
        print("\nBelum ada kasir yang terdaftar.")
        
# Fungsi untuk mendaftarkan kasir baru (nama, umur, alamat, no wa)
def daftarKasirBaru():
    clearScreen()
    tengahGaris(" DAFTAR KASIR BARU ")
    nama_kasir = input("\nNAMA      : ").upper()
    umur_kasir = int(input("UMUR        : "))
    alamat_kasir = input("ALAMAT    : ").upper()
    no_wa = int(input("NO WA            : "))
    
    isTambah = input("\nTambahkan Kasir? (y/n) : ")
    
    if isTambah == 'y':
        id = buatIDAngka()
        kasir_baru = [id, nama_kasir, umur_kasir, alamat_kasir, no_wa]
        daftar_kasir.append(kasir_baru)
        print(f"Kasir bernama '{nama_kasir}' berhasil didaftarkan.\n")
        lihatDaftarKasir()
    elif isTambah == 'n':
        print((5*'-'+" KASIR TIDAK DITAMBAHKAN "+5*'-').center(60,' '))
    else:
        # Jika input tidak valid
        print("Pilihan tidak valid, silakan pilih 'y' atau 'n'.")

# Menu pilihan
while True:
    clearScreen()
    tengahGaris(" SELAMAT DATANG ")
    tengahGaris(" DI JAYAMART ")
    tengahGaris(" APLIKASI KASIR ")

    inputUser = input("""
1. Masuk Aplikasi Kasir
2. Lihat Daftar Kasir
3. Daftar Menjadi Kasir
4. Keluar\n
Pilihan Anda (pilih 1 - 4): """)

    if inputUser == '1':
        aplikasiKasir()

    elif inputUser == '2':
        lihatDaftarKasir()
        input("\nTekan Enter untuk kembali ke menu...")

    elif inputUser == '3':
        daftarKasirBaru()
        input("\nTekan Enter untuk kembali ke menu...")

    elif inputUser == '4':
        clearScreen()
        tengahGaris(" TERIMA KASIH ")
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")















# # os.system('cls')
# print("JAYAMART SELAKAU / 0808080".center(60,' '))
# print("JL. AMPERA SELAKAU TUA".center(60,' '))
# print(60*'-')
# print(60*'-')
# print("Kasir : IHSAN".center(60,' '))
# print(60*'-')
# print(60*'-')



# item1 = ["MR HOT BLD 140G",1,12900,12900]
# item2 = ["MR HOT BBQ 140G",1,12900,12900]
# item3 = ["GERY SNK 100G",1,10400,10400]
# item4 = ["ICHITAN MC300ML",1,9300,9300]

# daftarItem = [item1,item2,item3,item4]

# for item in daftarItem:
#     print(f"{item[0]:<20} {item[1]:^3} {item[2]:<20,} {item[3]:<20,}")

# print(60*'-')
# print(60*'-')
# print("Total Item   4   46,000")
# print("Tunai            100,000")
# print("Kembalian        54,000")
# print("PPN  (   4,559)")
# print(60*'-')
# print(60*'-')
# print("Tgl. 10-10-2024 15:26:58 V.2024.7.5")
# print(60*'-')
# print("KRITIK&SARAN:12313".center(60,' '))
# print("SMS/WA: 08345354".center(60,' '))