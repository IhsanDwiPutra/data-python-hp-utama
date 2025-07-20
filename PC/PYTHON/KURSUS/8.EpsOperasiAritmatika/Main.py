print(20*"=" + "OPERASI ARITMATIKA" + 20*"=")

pilihan = input("""\nPilih operasi yang digunakan dan masukan angka :
1. Pertambahan (+)
2. Pengurangan (-)
3. Perkalian (*)
4. Pembagian (/)
5. Eksponen/Pangkat (**)
6. Modulus/sisa pembagian (%)
7. Floor Division/Pembulatan pembagian (//)
JAWABAN ANDA : """)

if pilihan == "1":
    print("\n" + 10*"=" + "PERTAMBAHAN" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("ditambah dengan : ")
    hasil = float(nilai_pertama) + float(nilai_kedua)
    print(nilai_pertama , "+", nilai_kedua, "=", hasil)
    
elif pilihan == "2":
    print("\n" + 10*"=" + "PENGURANGAN" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("dikurang dengan : ")
    hasil = float(nilai_pertama) - float(nilai_kedua)
    print(nilai_pertama , "-", nilai_kedua, "=", hasil)
    
elif pilihan == "3":
    print("\n" + 10*"=" + "PERKALIAN" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("dikali dengan : ")
    hasil = float(nilai_pertama) * float(nilai_kedua)
    print(nilai_pertama , "x", nilai_kedua, "=", hasil)
    
elif pilihan == "4":
    print("\n" + 10*"=" + "PEMBAGIAN" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("dibagi dengan : ")
    hasil = float(nilai_pertama) / float(nilai_kedua)
    print(nilai_pertama , "÷", nilai_kedua, "=", hasil)
    
elif pilihan == "5":
    print("\n" + 10*"=" + "EKSPONEN/PANGKAT" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("pangkat berapa : ")
    hasil = int(nilai_pertama) ** int(nilai_kedua)
    print(nilai_pertama , "**", nilai_kedua, "=", hasil)
    
elif pilihan == "6":
    print("\n" + 10*"=" + "MODULUS/SISA PEMBAGIAN" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("Masukkan angka kedua : ")
    hasil = int(nilai_pertama) % int(nilai_kedua)
    print(nilai_pertama , "%", nilai_kedua, "=", hasil)
    
elif pilihan == "7":
    print("\n" + 10*"=" + "FLOOR DIVISION/PEMBULATAN BAGIAN" + 10*"=")
    nilai_pertama = input("Masukkan angka pertama : ")
    nilai_kedua = input("Masukkan angka kedua : ")
    hasil = int(nilai_pertama) // int(nilai_kedua)
    print(nilai_pertama , "//", nilai_kedua, "=", hasil)
    
else :
    print("Angka yang anda masukkan salah")
    
episode = 8
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Rabu"
tanggal = 18
bulan = "Oktober"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")