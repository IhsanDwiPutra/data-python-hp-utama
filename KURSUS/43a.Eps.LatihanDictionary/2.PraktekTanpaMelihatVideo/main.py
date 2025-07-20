import datetime as dt

siswa_template = {
    'nama':'nama',
    'pendidikan':'pendidikan',
    'nisn':00000,
    'alamat':'alamat',
    'lahir':dt.datetime(1111,1,11)
}

siswa_baru = {}

print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA SISWA':^20}")
print(20*"=")

siswa = dict.fromkeys(siswa_template)
siswa['nama'] = input("Nama : ")
siswa['nism'] = input("NISN : ")
siswa['pendidikan'] = input("Pendidikan anda : ")
siswa['alamat'] = input("Alamat anda : ")
TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
BULAN_LAHIR = int(input("Bulan Lahir (1-12) : "))
TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31) : "))
siswa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(siswa)