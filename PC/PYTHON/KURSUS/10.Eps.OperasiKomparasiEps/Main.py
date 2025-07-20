print(20*"=" + "OPERASI KOMPARASI" + 20*"=")

# >, <, >=, <=, ==, !=, is, is not


pilihan = input("""\nPilih operasi yang ingin di komparasi dan masukkan angka :
1. Lebih Dari  (>)
2. Kurang Dari (<)
3. Lebih Dari Sama Dengan (>=)
4. Kurang Dari Sama Dengan (<=)
5. Sama Dengan Sama Dengan (==)
6. Tidak Sama Dengan (!=)
7. Apakah/is (is)
8. Apakah Tidak/is not (is not)
JAWABAN ANDA : """)

# 1. lebih dari
if pilihan == "1":
    print("\n" + 10*"=" + "Lebih Dari(>)" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("dikomparasi dengan : ")
    hasil = int(nilai_pertama) > int(nilai_kedua)
    print(nilai_pertama , ">", nilai_kedua, "=", hasil)
    
# 2. kurang dari
elif pilihan == "2":
    print("\n" + 10*"=" + "Kurang Dari(<)" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("dikomparasi dengan : ")
    hasil = int(nilai_pertama) < int(nilai_kedua)
    print(nilai_pertama , "<", nilai_kedua, "=", hasil)
    
# 3. lebih dari sama dengan
elif pilihan == "3":
    print("\n" + 10*"=" + "Lebih Dari Sama dengan(>=)" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("dikomparasi dengan : ")
    hasil = int(nilai_pertama) >= int(nilai_kedua)
    print(nilai_pertama , ">=", nilai_kedua, "=", hasil)
    
# 4. kurang dari sama dengan
elif pilihan == "4":
    print("\n" + 10*"=" + "Kurang Dari Sama dengan(<=)" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("dikomparasi dengan : ")
    hasil = int(nilai_pertama) <= int(nilai_kedua)
    print(nilai_pertama , "<=", nilai_kedua, "=", hasil)
    
# 5. sama dengan sama dengan
elif pilihan == "5":
    print("\n" + 10*"=" + "Sama dengan Sama dengan" + 10*"=")
    pilihan_kedua = int(input("Pilih yang mana dan masukkan angka\n1. String dengan String\n2. Angka dengan Angka\n3. String dengan angka\nMasukan Anda : "))
    if pilihan_kedua == 1:
        print("\n" + 10*"=" + "String dengan String" + 10*"=")
        nilai_pertama = str(input("Masukkan nilai pertama : "))
        nilai_kedua = str(input("dikomparasi dengan : "))
        hasil = nilai_pertama == nilai_kedua
        print(nilai_pertama , "==", nilai_kedua, "=", hasil)
    
    elif pilihan_kedua == 2:
        print("\n" + 10*"=" + "Angka dengan Angka" + 10*"=")
        nilai_pertama = int(input("Masukkan nilai pertama : "))
        nilai_kedua = int(input("dikomparasi dengan : "))
        hasil = nilai_pertama == nilai_kedua
        print(nilai_pertama , "==", nilai_kedua, "=", hasil)
        
    elif pilihan_kedua == 3:
        print("\n" + 10*"=" + "String dengan Angka" + 10*"=")
        nilai_pertama = str(input("Masukkan nilai pertama : "))
        nilai_kedua = int(input("dikomparasi dengan : "))
        hasil = nilai_pertama == nilai_kedua
        print(nilai_pertama , "==", nilai_kedua, "=", hasil)
        
    else :
        print("Nilai yang anda masukkan salah")
        
# 6. tidak sama dengan
elif pilihan == "6":
    print("\n" + 10*"=" + "Tidak Sama dengan" + 10*"=")
    pilihan_kedua = int(input("Pilih yang mana dan masukkan angka\n1. String dengan String\n2. Angka dengan Angka\n3. String dengan angka\nMasukan Anda : "))
    if pilihan_kedua == 1:
        print("\n" + 10*"=" + "String dengan String" + 10*"=")
        nilai_pertama = str(input("Masukkan nilai pertama : "))
        nilai_kedua = str(input("dikomparasi dengan : "))
        hasil = nilai_pertama != nilai_kedua
        print(nilai_pertama , "!=", nilai_kedua, "=", hasil)
    
    elif pilihan_kedua == 2:
        print("\n" + 10*"=" + "Angka dengan Angka" + 10*"=")
        nilai_pertama = int(input("Masukkan nilai pertama : "))
        nilai_kedua = int(input("dikomparasi dengan : "))
        hasil = nilai_pertama != nilai_kedua
        print(nilai_pertama , "!=", nilai_kedua, "=", hasil)
        
    elif pilihan_kedua == 3:
        print("\n" + 10*"=" + "String dengan Angka" + 10*"=")
        nilai_pertama = str(input("Masukkan nilai pertama : "))
        nilai_kedua = int(input("dikomparasi dengan : "))
        hasil = nilai_pertama != nilai_kedua
        print(nilai_pertama , "!=", nilai_kedua, "=", hasil)
        
    else :
        print("Nilai yang anda masukkan salah")

    
# apakah/is
elif pilihan == "7":
    print("\n" + 10*"=" + "Apakah / is" + 10*"=")
    nilai_pertama = input("Masukkan nilai x : ")
    nilai_kedua = input("dikomparasi dengan nilai y : ")
    print("x =", nilai_pertama, "\ny =", nilai_kedua)
    hasil = str(nilai_pertama) is str(nilai_kedua)
    print(nilai_pertama , "is", nilai_kedua, "=", hasil)
    
# apakah tidak/is not
elif pilihan == "8":
    print("\n" + 10*"=" + "Apakah Tidak / is not" + 10*"=")
    nilai_pertama = input("Masukkan nilai x : ")
    nilai_kedua = input("dikomparasi dengan nilai y : ")
    print("x =", nilai_pertama, "\ny =", nilai_kedua)
    hasil = str(nilai_pertama) is not str(nilai_kedua)
    print(nilai_pertama , "is", nilai_kedua, "=", hasil)
    
else :
    print("Angka yang anda masukkan salah")
    
episode= 10
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Sabtu"
tanggal = 21
bulan = "Oktober"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")


episode= 10
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Rabu"
tanggal = 16
bulan = "Oktober"
tahun = 2024
print("\n\nBelajar Bahasa Python kedua kali pada")
print(f"Dibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")


