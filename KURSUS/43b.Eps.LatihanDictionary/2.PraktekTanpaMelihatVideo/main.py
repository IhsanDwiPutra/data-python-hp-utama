import datetime as dt
import os
import string
import random

siswa_template = {
    'nama':'nama',
    'pendidikan':'pendidikan',
    'nisn':00000,
    'alamat':'alamat',
    'lahir':dt.datetime(1111,1,11)
}

siswa_baru = {}

while True:

    os.system('clear')
    print(f"{'SELAMAT DATANG':^60}")
    print(f"{'DATA SISWA':^60}")
    print(60*"=")
    
    siswa = dict.fromkeys(siswa_template)
    siswa['nama'] = input("Nama\t\t\t: ").upper()
    siswa['nisn'] = input("NISN\t\t\t: ")
    siswa['pendidikan'] = input("Pendidikan anda\t\t: ").upper()
    siswa['alamat'] = input("Alamat anda\t\t: ").upper()
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY)\t: "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12)\t: "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31)\t: "))
    siswa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR).strftime("%x")
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(3)))
    siswa_baru.update({KEY:siswa})

    print(f"\n{'KEY':^5} {'NAMA':<15} {'NISN':<10} {'PDN':^5} {'ALAMAT':<8} {'LAHIR':^10}")
    print(60*"-")
    
    
    for sis in siswa_baru:
        KEY = sis
        NAMA = siswa_baru[KEY]['nama']
        NISN = siswa_baru[KEY]['nisn']
        PDN = siswa_baru[KEY]['pendidikan']
        ALAMAT = siswa_baru[KEY]['alamat']
        LAHIR = siswa_baru[KEY]['lahir']
    
        print(f"{KEY:^5} {NAMA:<15} {NISN:<10} {PDN:^5} {ALAMAT:<8} {LAHIR:<10}")
    
    
    
    
    lanjut = input("\nMau tambah lagi bro ? (y/n) ")
    if lanjut == 'n':
        break
        
print("PROGRAM BERAKHIR")

