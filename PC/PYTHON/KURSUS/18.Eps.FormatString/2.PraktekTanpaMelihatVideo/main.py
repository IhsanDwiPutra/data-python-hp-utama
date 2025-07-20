print("FORMAT STRING".center(45,"="))

print("\nContoh Generic :")

print("1. String")
nama = "Ihsan"
format = f"Hallo {nama}\n"
print(format)

print("2. Boolean")
boolean = True
format = f"Udah makan = {boolean}\n"
print(format)

print("3. Angka")
angka = 2005.5
format = f"Angka = {angka}\n"
print(format)

print("4. Bilangan Bulat")
bulat = 25
format = f"Bilangan bulat = {bulat:d}\n"
print(format)

print("5.Bilangan dengan ordo jutaan")
angka = 10000000
format = f"Bilangan jutaan = {angka:,}\n"
print(format)

print("6. Bilangan Desimal ")
bilangan = 2096.49583
format = f"Bilangan desimal = {bilangan:.2f}\n"
print(format)

print("7. Menampilkan Leading Zero")
lead = 2096.49584
format = f"Leading Zero = {lead:010.2f}\n"
print(format)

print("8. Menampilkan tanda + dan -")
plus = 25
minus = -25
format_plus = f"Plus = {plus:+d}"
format_minus = f"Minus = {minus:+d}\n"
print(format_plus)
print(format_minus)

print("9. Menampilkan Persentase")
persen = 0.245
format = f"Persentase = {persen:.2%}\n"
print(format)

print("10. Menampilkan angka lain (binary, octal, hecadesimal)")
binary = f"Binary = {bin(255)}"
octal = f"Octal = {oct(255)}"
hexa = f"Hexadesimal = {hex(255)}\n"
print(binary)
print(octal)
print(hexa)

episode = 18
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Kamis"
tanggal = 14
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
