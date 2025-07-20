# Multi key & Nesting Dictionary

import datetime as dt

siswa1 = {
    "nama": "Ucup",
    "nisn": 5335636,
    "beasiswa": False,
    "lahir": dt.datetime(2004, 2, 23)
}

siswa2 = {
    "nama": "Asep",
    "nisn": 253455,
    "beasiswa": False,
    "lahir": dt.datetime(2007, 6, 14)
}

siswa3 = {
    "nama": "Ihsan",
    "nisn": 710224,
    "beasiswa": False,
    "lahir": dt.datetime(2007, 4, 13)
}

siswa4 = {
    "nama": "Coki",
    "nisn": 2894242,
    "beasiswa": True,
    "lahir": dt.datetime(1947, 7, 2)
}

siswa5 = {
    "nama": "Marko",
    "nisn": 242555,
    "beasiswa": False,
    "lahir": dt.datetime(2009, 2, 21)
}

data_siswa = {
    "SIS1": siswa1,
    "SIS2": siswa2,
    "SIS3": siswa3,
    "SIS4": siswa4,
    "SIS5": siswa5
}

print(f"|{'KEY':^7}|{'NAMA':^15}|{'NISN':^13}|{'BEASISWA':^10}|{'LAHIR':^15}|")
print(66*"-")

for data in data_siswa:
    KEY = data
    NAMA = data_siswa[KEY]["nama"]
    NISN = data_siswa[KEY]["nisn"]
    BEASISWA = data_siswa[KEY]["beasiswa"]
    LAHIR = data_siswa[KEY]["lahir"].strftime("%x")

    print(f"|{KEY:^7}|{NAMA:^15}|{NISN:^13}|{BEASISWA:^10}|{LAHIR:^15}|")
