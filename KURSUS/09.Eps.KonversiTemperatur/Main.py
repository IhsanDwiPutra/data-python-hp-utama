print(20*"=" + "KONVERSI TEMPERATUR" + 20*"=")

# konversi celsius ke satuan lain
celsius = float(input("Masukkan suhu ke celsius : "))
print("\nSuhu adalah", celsius,"Celsius ")

# reamur
reamur = (4/5) * celsius
print("\nSuhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celsius) + 32
print("\nSuhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celsius + 273
print("\nSuhu dalam kelvin adalah", kelvin, "Kelvin")

episode = 9
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Jumat"
tanggal = 20
bulan = "Oktober"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")