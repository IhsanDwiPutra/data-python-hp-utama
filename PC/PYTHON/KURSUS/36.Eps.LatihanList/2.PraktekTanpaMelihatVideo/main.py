# Latihan Membuat List buku

list_buku = []
while True:
    print("\nMasukkan Data Buku :")
    judul = input("Judul Buku\t: ")
    penulis = input("Nama Penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n\n", 10*"=", "DAFTAR BUKU", 10*"=")
    print("No\t| Judul\t\t| Penulis")
    for index, buku in enumerate(list_buku):
        print(f"{index+1}\t| {buku[0]}\t\t| {buku[1]}")

    print("\n", 20*"=")
    lanjut = input("Apakah Mau lanjut?(y/n) : ")

    if lanjut == "n":
        break

print("Program Selesai Terima Kasih")
