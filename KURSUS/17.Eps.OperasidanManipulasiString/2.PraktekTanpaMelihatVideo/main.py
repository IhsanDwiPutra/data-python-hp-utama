print("Operasi dan Manipulasi String".center(50, "-"))

# Merubah case dari string

# 1. merubah semua ke upper case
normal = "ini adalah normal"
print("normal = " + normal)

upper = normal.upper()
print("upper = " + upper)

# 2. merubah semua ke lower case
normal = "AkU KeCe BaDAIIiiiiiiiii"
print("normal = "+normal)

lower = normal.lower()
print("lower = "+lower)

# pengecekan dengan isX method

# 1. contoh pengecekan lower case
data_lower = "ini adalah lower case ya"
data_upper = "INI ADALAH TEKS KAPITAL"
lower = data_lower.islower()
upper = data_upper.islower()
print(data_lower+" apakah lower = " + str(lower))
print(data_upper + " apakah lower = "+str(upper))

# 2. contoh pengecekan  upper case
data_lower = "saya adalah seorang yang akan terus berjuang"
data_upper = "CARA MEMATIKAN KOMPUTER"
lower = data_lower.isupper()
upper = data_upper.isupper()
print(data_lower+" apakah upper = "+str(lower))
print(data_upper+" apakah upper = "+str(upper))

# 3. isalpha() <-- untuk mengecek huruf
# 4. isalnum() <-- untuk mengecek huruf dan angka
# 5. isdecimal() <-- untuk mengecek angka saja
# 6. isspace() <-- untuk mengecek spasi, tab, newline(/n)

# 7. istitle() <-- untuk mengecek semua kata dimulai dengan huruf besar
data = "Seorang Yang Bekerja Keras"
title = data.istitle()
print(data+" apakah judul = "+str(title))

# mengecek komponen

# 1. startswith()
data = "Ihsan Putra"
star = data.startswith("Ihsan")
print(data + " apakah starts = "+str(star))

# 2. endswith()
end = data.endswith("Putra")
print(data+" apakah end = "+str(end))

# penggabungan komponen

# 1. join()
list = ["halo", "apa", "kabar"]
print(list)
join = " ".join(list)
print(join)

# 2. split()
data = "siapa nama mu"
print(data)
split = data.split(" ")
print(split)

# alokasi karakter

# 1. rjust() <-- rata kanan
print("kanan".rjust(10))

# 2. ljust() <-- rata kiri
print("kiri".ljust(10))

# 3. center() <-- rata tengah
tengah = "tengah".center(20, "-")
print(tengah)

# 3.1 split() <-- kebalikan rata tengah
tengah = tengah.split("-")
print(tengah)
