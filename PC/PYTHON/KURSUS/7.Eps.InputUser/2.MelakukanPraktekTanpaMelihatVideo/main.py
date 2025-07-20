
list_buku = []

while True:
    print("\n\n"+" BIODATA ".center(60,"="))
    nama = input("\n\tNama\t\t: ")
    alamat = input("\tAlamat\t\t: ")
    lahir = input("\tTgl Lahir\t: ")
    
    buku_baru = [nama.upper(),alamat.upper(),str(lahir.upper())]
    list_buku.append(buku_baru)
    
    print("\n"+" BIODATA PENDUDUK ".center(45,"="))
    print(60*"-")
    print("NO.\t| NAMA\t\t| ALAMAT\t| TGL LAHIR\t|")
    print(60*"-")
    
    for index, data in enumerate(list_buku):
        print(f"{index+1}\t| {data[0]}\t\t| {data[1]}\t| {data[2]}\t")
    
    lanjut = input("\nTambahkan Lagi?(y/n) ")
    
    if lanjut.lower() == "n":
        print("PROGRAM SELESAI")
        break
    