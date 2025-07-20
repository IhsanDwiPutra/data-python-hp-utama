print(15*"=" + "LATIHAN KOMPARASI DAN LOGIKA" + 15*"=")

# ++++++5--------12+++++++

inputUser = float(input("Masukkan angka\nKurang dari 5\natau\nLebih besar dari 12 = "))

# ++++++++5
#memeriksa angka kurang dari 5
isKurangDari = (inputUser < 5)
print("\nKurang Dari 5 =", isKurangDari)


# -------12+++++++
# memeriksa angka lebih besar dari 12
isLebihBesarDari = (inputUser > 12)
print("Lebih Besar Dari 12 =", isLebihBesarDari)

hasil = isKurangDari or isLebihBesarDari
print("Jawaban yang anda masukkan :", hasil)

# -------5++++++++12-------
# kasus irisan

inputUser = float(input("\nMasukkan angka\nLebih besar dari 5\ndan\nKurang dari 12 = "))

# -------5
#memeriksa angka lebih besar dari 5
isLebihBesarDari = (inputUser > 5)
print("\nLebih besar Dari 5 =", isLebihBesarDari)


# ++++++++12-------
# memeriksa angka kurang dari 12
isKurangDari = (inputUser < 12)
print("Kurang Dari 12 =", isKurangDari)

hasil = isKurangDari and isLebihBesarDari
print("Jawaban yang anda masukkan :", hasil)

print("\n\n" + 10*"=" + "LATIHAN" + 10*"=")
print("1. -----0+++++++5-------8++++++++11-----\n2. +++++0-------5+++++++8--------11+++++")

print("Jawab :\n")

# 1. -----0+++++++5-------8++++++++11-----
inputUser = float(input("1. -----0+++++++5-------8++++++++11-----\n:"))
lebihDari0 = (inputUser > 0)
kurangDari5 = (inputUser < 5)
lebihDari8 = (inputUser > 8)
kurangDari11 = (inputUser < 11)
hasil1 = lebihDari0 and kurangDari5
hasil2 = lebihDari8 and kurangDari11
hasil3 = hasil1 or hasil2
print("Jawaban anda =", hasil3)

# 2. +++++0-------5+++++++8--------11+++++
inputUser = float(input("2. +++++0-------5+++++++8--------11+++++\n:"))
kurangDari0 = (inputUser < 0)
lebihDari5 = (inputUser > 5)
kurangDari8 = (inputUser < 8)
lebihDari11 = (inputUser > 11)
hasil1 = kurangDari0 or lebihDari5
hasil2 = kurangDari8 or lebihDari11
hasil3 = hasil1 and hasil2
print("Jawaban anda =", hasil3)

episode= 12
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Sabtu"
tanggal = 28
bulan = "Oktober"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")