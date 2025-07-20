# List utama untuk menyimpan daftar kasir
daftar_kasir = []

# Fungsi untuk menambahkan kasir baru ke dalam daftar
def tambahKasir():
    nama = input("Masukkan nama kasir: ")
    id_kasir = input("Masukkan ID kasir: ")
    shift = input("Masukkan shift kerja (Pagi/Siang/Malam): ")
    
    # Menambahkan kasir sebagai nested list ke daftar_kasir
    kasir_baru = [nama, id_kasir, shift]
    daftar_kasir.append(kasir_baru)
    print(f"Kasir '{nama}' berhasil ditambahkan.\n")

# Fungsi untuk menampilkan daftar kasir
def lihatDaftarKasir():
    if not daftar_kasir:
        print("Belum ada kasir yang terdaftar.\n")
    else:
        print("\nDaftar Kasir:")
        for index, kasir in enumerate(daftar_kasir, start=1):
            nama, id_kasir, shift = kasir
            print(f"{index}. Nama: {nama}, ID: {id_kasir}, Shift: {shift}")

# Program utama
while True:
    pilihan = input("\n1. Tambah Kasir\n2. Lihat Daftar Kasir\n3. Keluar\nPilih opsi (1-3): ")
    
    if pilihan == '1':
        tambahKasir()
    
    elif pilihan == '2':
        lihatDaftarKasir()
    
    elif pilihan == '3':
        print("Terima kasih!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.\n")
