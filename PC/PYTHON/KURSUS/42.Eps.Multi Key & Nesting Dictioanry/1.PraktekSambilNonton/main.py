# Multi Key & Nesting Dictionary

import datetime as dt

mahasiswa1 = {
    "nama": "Ucup Surucup",
    "nim": "142455",
    "sks_lulus": 150,
    "beasiswa": False,
    "lahir": dt.datetime(2001, 4, 10)
}

mahasiswa2 = {
    "nama": "Otong Surotong",
    "nim": "142456",
    "sks_lulus": 120,
    "beasiswa": True,
    "lahir": dt.datetime(2004, 2, 8)
}

mahasiswa3 = {
    "nama": "Asep si Kasyep",
    "nim": "142428",
    "sks_lulus": 30,
    "beasiswa": False,
    "lahir": dt.datetime(1998, 7, 6)
}

data_mahasiswa = {
    "MAH01": mahasiswa1,
    "MAH02": mahasiswa2,
    "MAH03": mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for data in data_mahasiswa:
    KEY = data

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{data:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
