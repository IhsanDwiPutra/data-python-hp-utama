import mysql.connector

# Koneksi ke database MariaDB/MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="biodata_db",
    charset='utf8mb4',
    collation='utf8mb4_general_ci' 
)

cursor = db.cursor()

# Fungsi untuk menambah biodata
def tambah_biodata(nama, alamat, usia):
    query = "INSERT INTO biodata (nama, alamat, usia) VALUES (%s, %s, %s)"
    values = (nama, alamat, usia)
    cursor.execute(query, values)
    db.commit()
    print(f"Biodata {nama} berhasil ditambahkan.")

# Fungsi untuk melihat semua biodata
def lihat_biodata():
    cursor.execute("SELECT * FROM biodata")
    result = cursor.fetchall()
    for data in result:
        print(data)

# Fungsi untuk memperbarui biodata berdasarkan ID
def update_biodata(id, nama, alamat, usia):
    query = "UPDATE biodata SET nama = %s, alamat = %s, usia = %s WHERE id = %s"
    values = (nama, alamat, usia, id)
    cursor.execute(query, values)
    db.commit()
    print(f"Biodata dengan ID {id} berhasil diperbarui.")

# Fungsi untuk menghapus biodata berdasarkan ID
def hapus_biodata(id):
    query = "DELETE FROM biodata WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    print(f"Biodata dengan ID {id} berhasil dihapus.")

# Menu interaktif
while True:
    print("\nMenu Biodata:")
    print("1. Tambah Biodata")
    print("2. Lihat Biodata")
    print("3. Update Biodata")
    print("4. Hapus Biodata")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan alamat: ")
        usia = int(input("Masukkan usia: "))
        tambah_biodata(nama, alamat, usia)

    elif pilihan == "2":
        lihat_biodata()

    elif pilihan == "3":
        id = int(input("Masukkan ID biodata yang ingin diupdate: "))
        nama = input("Masukkan nama baru: ")
        alamat = input("Masukkan alamat baru: ")
        usia = int(input("Masukkan usia baru: "))
        update_biodata(id, nama, alamat, usia)

    elif pilihan == "4":
        id = int(input("Masukkan ID biodata yang ingin dihapus: "))
        hapus_biodata(id)

    elif pilihan == "5":
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
