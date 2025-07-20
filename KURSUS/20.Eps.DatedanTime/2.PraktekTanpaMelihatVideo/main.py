# Date dan Time latihan

import datetime as dt

print("Masukkan tanggal lahir anda :")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

print(f"Hari anda lahir adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Tanggal hari ini adalah : {hari_ini}")

jumlah_hari = hari_ini - tanggal_lahir

jumlah_tahun = jumlah_hari.days // 365
jumlah_bulan = (jumlah_hari.days % 365) // 30
print(f"Umur anda adalah = {jumlah_tahun}, {jumlah_bulan} bulan")
