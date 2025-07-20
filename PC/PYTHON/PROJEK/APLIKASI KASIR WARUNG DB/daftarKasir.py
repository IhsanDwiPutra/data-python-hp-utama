import os
import random
import mysql.connector

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="daftar_kasir",
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)

cursor = db.cursor()

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

def tekanEnter():
    input("   Tekan Enter untuk melanjutkan...")

# Fungsi untuk menampilkan daftar kasir
def lihatDaftarKasir():
    clearScreen()
    cursor.execute("SELECT * FROM kasir") 
    result = cursor.fetchall()

    if result:  # Cek apakah ada kasir yang terdaftar
        print((5*'-'+" DAFTAR KASIR YANG TERDAFTAR "+5*'-').center(60,' '))
        # [id, nama_kasir, umur_kasir, alamat_kasir, no_wa]
        print('\n')
        print(60*'-')
        print("| NO | ID | NAMA       | UMUR | ALAMAT     | NO WA         |")
        print(60*'-')
        for data in result:
            print(f"| {data[0]:<3}| {data[1]:<3}| {data[2]:<11}| {data[3]:^5}| {data[4]:<11}| 0{data[5]:<13}|")
                
        print(60*'-')        
    else:
        print("   Belum ada kasir yang terdaftar.")
        
# Fungsi untuk mendaftarkan kasir baru (nama, umur, alamat, no wa)
def daftarKasirBaru():
    clearScreen()
    print((5*'-'+" DAFTAR KASIR BARU "+5*'-').center(60,' '))
    nama_kasir = input("\n   NAMA      : ").upper()
    umur_kasir = int(input("   UMUR      : "))
    alamat_kasir = input("   ALAMAT    : ").upper()
    no_wa = int(input("   NO WA     : "))
    
    isTambah = input("\n   Tambahkan Kasir? (y/n) : ")
    
    if isTambah == 'y':
        noId = buatIDAngka()
        query = "INSERT INTO kasir (noId, name, age, address, number) VALUES (%s, %s, %s, %s, %s)"
        values = (noId, nama_kasir, umur_kasir, alamat_kasir, no_wa)
        cursor.execute(query, values)
        db.commit()
        
        # kasir_baru = [noId, nama_kasir, umur_kasir, alamat_kasir, no_wa]
        # daftar_kasir.append(kasir_baru)
        print(f"   Kasir bernama '{nama_kasir}' berhasil didaftarkan.\n")
        tekanEnter()
        lihatDaftarKasir()
    elif isTambah == 'n':
        print("\n")
        print((5*'-'+" KASIR TIDAK DITAMBAHKAN "+5*'-').center(60,' '))
    else:
        # Jika input tidak valid
        print("   Pilihan tidak valid, silakan pilih 'y' atau 'n'.")
        
def ubahDataKasir():
    clearScreen()
    print((5*'-'+" UPDATE DATA KASIR "+5*'-').center(60,' '))
    pilihan = input("""
       1. Ubah ID
       2. Ubah Nama
       3. Ubah Umur
       4. Ubah Alamat
       5. Ubah No WA
       6. Ubah Semua
       
       Pilihan Anda: """)
    lihatDaftarKasir()
    id_input = int(input("\n   Masukkan ID biodata yang ingin diupdate: "))
    
    # Mengambil semua id dari tabel kasir
    cursor.execute("SELECT id FROM kasir") 
    result = cursor.fetchall()
    
    # Mengonversi hasil menjadi list ID
    id_list = [row[0] for row in result]  # row[0] karena fetchall() mengembalikan tuple
    
    # Mengecek apakah id_input ada di dalam id_list
    if id_input in id_list:
        tampilkanId(id_input)
        
        nama_kasir = input("\n   Nama Baru      : ").upper()
        umur_kasir = int(input("   Umur Baru      : "))
        alamat_kasir = input("   Alamat Baru    : ").upper()
        no_wa = int(input("   No WA Baru     : "))
        
        isUbah = input("\n   Ubah data? (y/n) : ")
        
        if isUbah == 'y':
            query = "UPDATE kasir SET name = %s, age = %s, address = %s, number = %s WHERE id = %s"
            values = (nama_kasir, umur_kasir, alamat_kasir, no_wa, id_input)
            cursor.execute(query, values)
            db.commit()
            
            print("\n   Data Berhasil Di Ubah")
            tekanEnter()
            
            lihatDaftarKasir()
            tekanEnter()
            
        elif isUbah == 'n':
            print("\n")
            print((5*'-'+" KASIR TIDAK DIUBAH "+5*'-').center(60,' '))
        else:
            # Jika input tidak valid
            print("   Pilihan tidak valid, silakan pilih 'y' atau 'n'.")
            
    else:
        print("   ID tidak ditemukan")
        tekanEnter()
            
def hapusKasir():
    clearScreen()
    print((5*'-'+" HAPUS DATA KASIR "+5*'-').center(60,' '))
    lihatDaftarKasir()
    id_input = int(input("\n   Masukkan ID biodata yang ingin dihapus: "))
    
    # Mengambil semua id dari tabel kasir
    cursor.execute("SELECT id FROM kasir") 
    result = cursor.fetchall()
    
    # Mengonversi hasil menjadi list ID
    id_list = [row[0] for row in result]  # row[0] karena fetchall() mengembalikan tuple
    
    # Mengecek apakah id_input ada di dalam id_list
    if id_input in id_list:
        tampilkanId(id_input)
        
        isHapus = input("\n   Yakin Hapus data (y/n) : ")
        
        if isHapus == 'y':
            query = "DELETE FROM kasir WHERE id = %s"
            cursor.execute(query, (id_input,))
            db.commit()
            
            print("\n   Data Berhasil Di Hapus")
            tekanEnter()
            
            lihatDaftarKasir()
            tekanEnter()
            
        elif isHapus == 'n':
            print("\n")
            print((5*'-'+" KASIR TIDAK DIHAPUS "+5*'-').center(60,' '))
        else:
            # Jika input tidak valid
            print("   Pilihan tidak valid, silakan pilih 'y' atau 'n'.")
            
    else:
        print("   ID tidak ditemukan")
        tekanEnter()

def tampilkanId(id_input):
    # Query untuk mengambil semua data dari kasir dengan ID yang sesuai
    query = "SELECT * FROM kasir WHERE id = %s"
    cursor.execute(query, (id_input,))
    result = cursor.fetchone()  # Mengambil satu hasil dari query
    
    print('\n')
    print(60*'-')
    print("| NO | ID | NAMA       | UMUR | ALAMAT     | NO WA         |")
    print(60*'-')
    
    # Menampilkan data dalam format tabel
    print(f"| {result[0]:<3}| {result[1]:<3}| {result[2]:<11}| {result[3]:^5}| {result[4]:<11}| 0{result[5]:<13}|")
    print(60*'-')
    

# Menu pilihan
while True:
    clearScreen()
    tengahGaris(" SELAMAT DATANG ")
    tengahGaris(" DI JAYAMART ")
    tengahGaris(" APLIKASI KASIR ")

    inputUser = input("""
   1. Lihat Daftar Kasir
   2. Daftar Menjadi Kasir
   3. Ubah Data Kasir
   4. Hapus Data Kasir
   5. Keluar\n

   Pilihan Anda (pilih 1 - 3): """)

    if inputUser == '1':
        lihatDaftarKasir()
        input("\nTekan Enter untuk kembali ke menu...")

    elif inputUser == '2':
        daftarKasirBaru()
        tekanEnter()
        
    elif inputUser == '3':
        ubahDataKasir()
        
    elif inputUser == '4':
        hapusKasir()
        
    elif inputUser == '5':
        clearScreen()
        print((5*'-'+" TERIMA KASIH "+5*'-').center(60,' '))
        print("\n")
        print("Terima kasih telah menggunakan aplikasi kasir.".center(60,' '))
        break

    else:
        print("   Pilihan tidak valid, silakan coba lagi.")
        