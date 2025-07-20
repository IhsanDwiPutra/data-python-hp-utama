print(20*"="+"SPLDV"+20*"=")

print("\n")


nilai1_1 = int(input("Masukkan nilai 1 angka pertama : "))
nama1_1 = str(input("nama nilai 1 angka pertama disebut : "))
nilai1_2 = int(input("Masukkan nilai 1 angka kedua : "))
nama1_2 = str(input("Nama nilai 1 angka kedua dusebut : "))
nilai_harga1 = str(input("Masukkan nilai harga 1 : "))

print("\n")

nilai2_1 = int(input("Masukkan nilai 2 angka pertama : "))
nilai2_1 = str(input("nama nilai 2 angka pertama disebut : "))
nilai2_2 = int(input("Masukkan nilai 2 angka kedua : "))
nama2_2 = str(input("Nama nilai 2 angka kedua dusebut : "))
nilai_harga2 = str(input("Masukkan nilai harga 2 : "))

print("\n")

if nilai1_2 <= 0:
    print("+",str(nilai1_2))
else:
    print()

print(5*"="+"JADI"+5*"=")
print(str(nilai1_1)+nama1_1+str(nilai1_2))