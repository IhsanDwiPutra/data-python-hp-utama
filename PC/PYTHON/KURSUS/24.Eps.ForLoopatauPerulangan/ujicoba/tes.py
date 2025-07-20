def hitungSiswa(dataList):
    for index,data in enumerate(dataList):
        print(f"{index+1}. {data}")

siswa = ["agus","bagas","fahrul","adi"]

while True:
    nama = input("Masukkan nama yang ingin ditambahkan : ")
    siswa.append(nama)
    hitungSiswa(siswa)
        
    if len(siswa) == 10:
        print("Maaf quota sudah penuh")
        break
        
        
    isLanjut = input("Mau tambahkan lagi ? (y/n)")
    if isLanjut == "n":
        break
    
print("program selesai")




# for index,sis in enumerate(siswa):
#     print(f"{index+1}. {sis}")


# for i in jumlah:
#     print(i+1)


        
        
