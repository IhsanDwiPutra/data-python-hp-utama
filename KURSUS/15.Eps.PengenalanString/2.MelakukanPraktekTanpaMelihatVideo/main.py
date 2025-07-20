print(15*"=" + "PRAKTEK STRING" + 15*"=")

data = "ini adalah string"
print("string = " + data + " , type = " , type(data))

'''
1. Pembuatan string
- single string
- double string
'''

# single string
print('Saya belum makan')

# double string
print("Saya belum makan")

# penggunaan bersamaan single dan double
print("Hari ini adalah hari jum'at")
print('Bima : "Hei kamu sini"')


# 2. penggunaan tanda "\"

# backslash
print("Hari ini adalah jum\'at")

# tab
print("ANDI dan DORMAN\t\t jauhan")

# backspace
print("Andi \bDorman dekatan")

# newline
print("Baris pertama.\nBaris Kedua.") # LF --> LINE FEED = mac, unix
print("Baris pertama.\rBaris Kedua.") # CR --> CARRIAGE RETURN = os jadul
print("Baris pertana.\r\nBaris Kedua.") # CRLF --> CARRIAGE RETURN LINE FEED = WINDOWS

# 3. String Literal dan Raw String

# Multiline literal string
print("""
NAMA   : IHSAN
ALAMAT : SELAKAU TUA
""")

# Raw String
print(r"D:\ihsan\nama")

# Multiline raw string
print(r"""
NAMA   : IHSAN
ALAMAT : SELAKAU TUA
WEBSITE: www.ihsan/news/bakal
""")

episode = 15
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Minggu"
tanggal = 12
bulan = "November"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")

