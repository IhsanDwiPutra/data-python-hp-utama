# Fungsi untuk menampilkan pesan di tengah dengan garis
def tengahGaris(pesan):
    print(pesan.center(60, '-'))

# Tampilan awal
tengahGaris(" SELAMAT DATANG ")
tengahGaris(" DI JAYAMART ")
tengahGaris(" APLIKASI KASIR ")

# List untuk menyimpan data kasir
daftar_kasir = []

# Fungsi untuk menampilkan daftar kasir
def lihatDaftarKasir():
    if daftar_kasir:
        print("\nDaftar Kasir yang Terdaftar:")
        for index, kasir in enumerate(daftar_kasir, start=1):
            print(f"{index}. {kasir}")
    else:
        print("\nBelum ada kasir yang terdaftar.")

# Fungsi untuk mendaftarkan kasir baru
def daftarKasirBaru():
    nama_kasir = input("\nMasukkan nama kasir baru: ")
    daftar_kasir.append(nama_kasir)
    print(f"Kasir '{nama_kasir}' berhasil didaftarkan.")

# Fungsi untuk menangani transaksi belanja di aplikasi kasir
def aplikasiKasir():
    if not daftar_kasir:
        print("\nBelum ada kasir yang terdaftar. Daftarkan kasir terlebih dahulu.")
        return
    
    # Pilih kasir yang bertugas
    lihatDaftarKasir()
    kasir_terpilih = input("\nPilih kasir yang bertugas (nomor): ")
    
    # Cek apakah kasir valid
    if not kasir_terpilih.isdigit() or int(kasir_terpilih) < 1 or int(kasir_terpilih) > len(daftar_kasir):
        print("Pilihan kasir tidak valid!")
        return
    
    kasir = daftar_kasir[int(kasir_terpilih) - 1]
    print(f"\nKasir yang bertugas: {kasir}")
    
    # Input data belanja
    nama_pembeli = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    
    total_harga = 0
    for i in range(jumlah_barang):
        nama_barang = input(f"Masukkan nama barang ke-{i+1}: ")
        harga_barang = int(input(f"Masukkan harga barang {nama_barang}: Rp "))
        total_harga += harga_barang
    
    # Tampilkan total belanja
    print(f"\nTotal harga belanja: Rp {total_harga}")

    # Input jumlah uang tunai yang dibayarkan
    tunai = int(input("Masukkan jumlah uang tunai yang dibayarkan: Rp "))

    # Hitung kembalian
    if tunai >= total_harga:
        kembalian = tunai - total_harga
        print(f"Kembalian: Rp {kembalian}")
    else:
        print("Uang tunai tidak mencukupi, transaksi gagal!")

# Menu pilihan
while True:
    inputUser = input("""\n1. Masuk Aplikasi Kasir
2. Lihat Daftar Kasir
3. Daftar Menjadi Kasir
4. Keluar\n
Pilihan Anda (pilih 1 - 4): """)

    if inputUser == '1':
        tengahGaris(" MASUK APLIKASI KASIR ")
        aplikasiKasir()

    elif inputUser == '2':
        tengahGaris(" LIHAT DAFTAR KASIR ")
        lihatDaftarKasir()

    elif inputUser == '3':
        tengahGaris(" DAFTAR MENJADI KASIR ")
        daftarKasirBaru()

    elif inputUser == '4':
        tengahGaris(" TERIMA KASIH ")
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
