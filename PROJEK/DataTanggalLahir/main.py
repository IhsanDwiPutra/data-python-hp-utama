import datetime as dt

print(" DATA KELAHIRAN ".center(60,"="))

list_user = []
while True:

    tgl_today = dt.date.today()
    print(f"\nTanggal Hari ini adalah {tgl_today}\n")
    
    nama = input("Nama\t\t\t: ")
    print("Masukkan Data Tahun anda lahir")
    tahun = int(input("Tahun (TTTT)\t\t: "))
    bulan = int(input("Bulan (BB)\t\t: "))
    tanggal = int(input("Tanggal (TT)\t\t: "))
    
    tanggal_lahir = dt.date(tahun,bulan,tanggal)
    print(f"Tanggal anda lahir\t: {tanggal_lahir}")
    
    print(f"Hari anda lahir\t\t: {tanggal_lahir:%A}")
    
    jumlah_hari = tgl_today - tanggal_lahir
    print(f"Jumlah hari anda hidup\t: {jumlah_hari.days} hari")
    
    jumlah_tahun = jumlah_hari.days // 365
    jumlah_bulan = (jumlah_hari.days % 365) // 30
    print(f"Usia anda\t\t: {jumlah_tahun} tahun, {jumlah_bulan} bulan")
    
    
    
    data_baru = [nama,tanggal_lahir,jumlah_tahun,jumlah_bulan]
    list_user.append(data_baru)
    
    print("\n")
    print(" LIST DATA ".center(60,"="))
    print("No | Nama\t\t| Tgl lahir\t| Usia\t\t|")
    for index, tanggal in enumerate(list_user):
        print(f"{index+1}  | {tanggal[0]}\t\t| {tanggal[1]}\t| {tanggal[2]} t,{tanggal[3]} b\t|")
        
    lanjut = input("\nTambahkan Lagi ? (y/n) : ")
    if lanjut.lower() == "n":
        break
        
print("\n"+"PROGRAM SELESAI".center(60," "))
print("TERIMA KASIH :)".center(60," "))