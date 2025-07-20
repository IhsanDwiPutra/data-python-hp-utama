import datetime as dt
import os
import string
import random

siswa_template = {
    'nama':'nama',
    'alamat':'alamat',
    'lahir':dt.datetime(1111,1,11)
}

data_siswa = {}

while True:
    os.system('clear')
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(3)))
    siswa = dict.fromkeys(siswa_template)
    siswa['nama'] = input("Nama : ")
    siswa['alamat'] = input("Alamat : ")
    TAHUN = int(input("Tahun Lahir : "))
    BULAN = int(input("Bulan Lahir : "))
    TANGGAL = int(input("Tanggal Lahir : "))
    siswa['lahir'] = dt.datetime(TAHUN,BULAN,TANGGAL).strftime("%x")
    
    data_siswa.update({KEY:siswa})
        
    print(f"No Nama Alamat Tahun Lahir")
    
    for sis in data_siswa:
        
        KEY = sis
        NAMA = data_siswa[KEY]['nama']
        ALAMAT = data_siswa[KEY]['alamat']
        LAHIR = data_siswa[KEY]['lahir']
        
        print(f" {KEY} {NAMA} {ALAMAT} {TAHUN} {LAHIR}")
        
    lanjut = input("Mau tambah lagi bro ? (y/n) ")
    if lanjut != "y":
        break
        
print("Akhir Program")