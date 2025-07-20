print(15*"="+"OPERASI MANIPULASI STRING"+15*"=")

# 1. Menyambung String
nama_awal = "Ucup"
nama_tengah = "D'"
nama_akhir = "Fame"
nama_lengkap = nama_awal + " " + nama_tengah + nama_akhir
print(nama_lengkap)

# 2. Menghitung Panjang String(lenght)
panjang = len(nama_lengkap)
print("Panjang kata " + nama_lengkap + "= " + str(panjang))

# 3. cek character
d = "d" in nama_lengkap
print("Apakah ada kata d di " + nama_lengkap + "= " + str(d))

d = "D" in nama_lengkap
print("Apakah ada kata D di " + nama_lengkap + "= " + str(d))

d = "d" not in nama_lengkap
print("Apakah tidak ada kata d di " + nama_lengkap + "= " + str(d))

# 4. Mengulang String
print("awok"*15)

# 5. Indexing
print("Index ke-0 = " + nama_lengkap[0])
print("Index ke 6 = " + nama_lengkap[6])
print("Index ke -1 = " + nama_lengkap[-1])
print("Index ke -2 = " + nama_lengkap[-2])
print("Index ke 0:4 = " + nama_lengkap[0:4])
print("Index ke 0:-4 = " + nama_lengkap[-1:-4])
print("Index ke 0:11:2 = " + nama_lengkap[0:11:2])
    

# 6. Item paling kecil
print("Item paling kecil adalah " + min(nama_lengkap))

# 7. Item besar
print("Item paling besar adalah " + max(nama_lengkap))

# 8. Mencari asciicode
ascikod = ord(" ")
print("Berapa kode ascikode ' ' = " + str(ascikod))

data = 121
print("Asci kode yang bernomor " + str(data) + " adalah " + str(chr(data)))

# 9. Menghitung dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada "+data+" = "+ str(jumlah))

episode = 16
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Rabu"
tanggal = 6
bulan = 12
if bulan == 1:
    bulan = "Januari"
elif bulan == 2:
    bulan = "Februari"
elif bulan == 3:
    bulan = "Maret"
elif bulan == 4:
    bulan = "April"
elif bulan == 5:
    bulan = "Mei"
elif bulan == 6:
    bulan = "Juni"
elif bulan == 7:
    bulan = "Juli"
elif bulan == 8:
    bulan = "Agustus"
elif bulan == 9:
    bulan = "September"
elif bulan == 10:
    bulan = "Oktober"
elif bulan == 11:
    bulan = "November"
elif bulan == 12:
    bulan = "Desember"
else:
    bulan = "?"

tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")