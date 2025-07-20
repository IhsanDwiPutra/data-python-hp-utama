
import datetime as dt
#import os
# template dict mahasiswa

mahasiswa_template = {
    'nama': 'nama',
    'nim': '000000',
    'sks_lulus': 0,
    'lahir': dt.datetime(1111, 1, 11)
}

data_mahasiswa = {}

#os.system("clear")
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print(20*"-")

mahasiswa = dict.fromkeys(mahasiswa_template)
mahasiswa['nama'] = input("Nama Mahasiswa : ")
mahasiswa['nim'] = input("NIM Mahasiswa : ")
mahasiswa['sks_lulus'] = input("SKS Lulus : ")
TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
BULAN_LAHIR = int(input("Bulan Lahir (1-12) : "))
TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31) : "))
mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
print(mahasiswa)
