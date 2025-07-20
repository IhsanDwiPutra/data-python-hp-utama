# Date Time

import datetime as dt

print(" CEK TAHUN ANDA LAHIR ".center(60,"="))
print("\n")

tgl_today = dt.date.today()
while True:
    print(f"\nTanggal Hari adalah {tgl_today}\n")
    
    print("Masukkan Tanggal dan Tahun anda lahir :)\n")
    tahun = int(input("Tahun (TTTT)\t: "))
    bulan = int(input("Bulan (BB)\t: "))
    tanggal = int(input("Tanggal (TT)\t: "))
    
    tanggal_lahir = dt.date(tahun,bulan,tanggal)
    print(f"\nTanggal anda lahir\t: {tanggal_lahir}\nHari anda lahir\t\t: {tanggal_lahir:%A}")
    
    jumlah_hari = tgl_today - tanggal_lahir
    print(f"Jumlah hari anda hidup\t: {jumlah_hari.days} hari")
    
    jumlah_tahun = jumlah_hari.days // 365
    print(f"Jumlah tahun anda hidup\t: {jumlah_tahun} tahun")
    
    jumlah_bulan = (jumlah_hari.days % 365) // 30
    print(f"Jumlah bulan anda hidup\t: {jumlah_bulan} bulan\n")

    lagi = input("\nLagi ? (y/n) : ")
    if lagi.lower() == "n":
        break
        
print(" TERIMA KASIH ".center(60,"="))