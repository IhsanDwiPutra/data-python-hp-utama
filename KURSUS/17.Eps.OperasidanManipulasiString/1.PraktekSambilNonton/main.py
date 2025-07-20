# operator dalam bentuk method
# merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("Upper = " + salam)

# merubah semua ke lower case
alay = "aKu KecE AbIeZZZzzzzzZZZZ"
print("Normal = " + alay)
alay = alay.lower()
print("Lower = " + alay)

# pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum <-- huruf dan angka
# isdecimal <-- angka saja
# isspace <-- spasi, tab, newline /n


# istitle <-- semua kata dimulai dengan hutuf besar/kapital
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " apakah dia is title = " + str(cek_judul))

# ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print(str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppak")
print(str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kau']
gabungan = ' '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm"))

# alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20, "-")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip("-")  # menghilangkan tanda -
print("'"+tengah+"'")

episode = 17
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Sabtu"
tanggal = 9
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
