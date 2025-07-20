# format string

# contoh generic
# string

nama = "ucup"
format_str = f"hello {nama}"

print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"

print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"

print(format_str)

# bilangan bulat
bilangan = 25
format = f"bilangan bulat = {bilangan:d}"

print(format)

# bilangan dengan ordo ribuan
bilangan = 10000000
format = f"bilangan jutaan = {bilangan:,}"

print(format)

# bilangan desimal
angka = 2005.5749392
format_str = f"desimal = {angka:.2f}"

print(format_str)

# menampilkan leading zero
angka = 2005.5749392
format_str = f"desimal = {angka:018.2f}"

print(format_str)

# menampilkan tanda + dan -
minus = -10
plus = 10
format_minus = f"minus = {minus:+d}"
format_plus = f"plus = {plus:+d}"
print(format_minus)
print(format_plus)

# menampilan persentase
persen = 0.045
format_persen = f"persen = {persen:.1%}"
print(format_persen)

# menampilkan angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexa = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)

episode = 18
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Rabu"
tanggal = 13
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