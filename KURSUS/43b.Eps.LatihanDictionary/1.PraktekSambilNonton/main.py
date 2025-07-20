
import datetime as dt
import os
import string
import random
# template dict mahasiswa

mahasiswa_template = {
    'nama': 'nama',
    'nim': '000000',
    'sks_lulus': 0,
    'lahir': dt.datetime(1111, 1, 11)
}

data_mahasiswa = {}


while True :
    os.system("clear")
    print(f"{'SELAMAT DATANG':^60}")
    print(f"{'DATA MAHASISWA':^60}")
    print(60*"-")
    
    mahasiswa = dict.fromkeys(mahasiswa_template)
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("NIM Mahasiswa : ")
    mahasiswa['sks_lulus'] = input("SKS Lulus : ")
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31) : "))
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
        
    
    print(f"{'KEY':<6} {'Nama':<17} {'NIM':<13} {'SKS Lulus':<10} {'Lahir':^10}")
    print("-"*60)

    for data in data_mahasiswa:
        KEY = data
    
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
        print(f"{data:<6} {NAMA:<17} {NIM:<13} {SKS:^10} {LAHIR:<10}")
    
    lanjut = input("\nMau tambah lagi bro ? (y/n) ")
    if lanjut == "n":
        break
        
print("Akhir Program Ini")