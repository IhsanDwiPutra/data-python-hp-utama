import os

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
        print("\nDaftar Kasir yang Terdaftar:")
        for index, kasir in enumerate(daftar_kasir, start=1):
            print(f"{index}. Nama: {kasir[0]}, Umur: {kasir[1]}, Alamat: {kasir[2]}, No WA: {kasir[3]}")
    else:
        print("\nBelum ada kasir yang terdaftar.")

# Fungsi untuk mendaftarkan kasir baru (nama, umur, alamat, no wa)
def daftarKasirBaru():
    clearScreen()
    tengahGaris(" DAFTAR KASIR BARU ")
    nama_kasir = input("\nNAMA      : ")
    umur_kasir = input("UMUR      : ")
    alamat_kasir = input("ALAMAT    : ")
    no_wa = input("NO WA     : ")
    
    isTambah = input("\nTambahkan Kasir? (y/n) : ").lower()
    
    if isTambah == 'y':
        kasir_baru = [nama_kasir, umur_kasir, alamat_kasir, no_wa]
        daftar_kasir.append(kasir_baru)
        print(f"Kasir '{nama_kasir}' berhasil didaftarkan.")
    elif isTambah == 'n':
        print("Kasir tidak ditambahkan.")
    else:
        print("Pilihan tidak valid, silakan pilih 'y' atau 'n'.")

# Fungsi untuk aplikasi kasir (simulasi transaksi)
def aplikasiKasir():
    clearScreen()
    tengahGaris(" MASUK APLIKASI KASIR ")
    
    # Contoh item belanja
    item1 = ["MR HOT BLD 140G", 1, 12900, 12900]
    item2 = ["MR HOT BBQ 140G", 1, 12900, 12900]
    item3 = ["GERY SNK 100G", 1, 10400, 10400]
    item4 = ["ICHITAN MC300ML", 1, 9300, 9300]
    daftarItem = [item1, item2, item3, item4]
    
    # Menampilkan daftar belanja
    print("Nama Item".ljust(20), "Qty".ljust(10), "Harga".ljust(10), "Total".ljust(10))
    for item in daftarItem:
        print(f"{item[0]:<20} {item[1]:<10} {item[2]:<10,} {item[3]:<10,}")
    
    print("-" * 60)
    print("Total Item   4   Rp 46,000")
    print("Tunai            Rp 100,000")
    print("Kembalian        Rp 54,000")
    print("PPN  (   4,559)")
    print(60*'-')
    print("Tgl. 10-10-2024 15:26:58 V.2024.7.5")
    print(60*'-')

# Program utama (menu pilihan)
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
