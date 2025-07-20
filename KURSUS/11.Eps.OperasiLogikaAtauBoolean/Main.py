print(18*"=" + "OPERASI LOGIKA/BOOLEAN" + 18*"=")

print(5*"-" + "NOT" + 5*"-")
a = True
print("data a =", a)

print(10*"-" + "NOT")
b = not a
print("data a = NOT TRUE =", b)

print("\n" + 5*"-" + "OR" + 5*"-")
a = True
b = True
c = a or b
print(a, "or", b, "  =", c)
a = False
b = False
c = a or b
print(a, "or", b, "=", c)
a = True
b = False
c = a or b
print(a, "or", b, " =", c)
a = False
b = True
c = a or b
print(a, "or", b, " =", c)

print("\n" + 5*"-" + "AND" + 5*"-")
a = True
b = True
c = a and b
print(a, "and", b, "  =", c)
a = False
b = False
c = a and b
print(a, "and", b, "=", c)
a = True
b = False
c = a and b
print(a, "and", b, " =", c)
a = False
b = True
c = a and b
print(a, "and", b, " =", c)

print("\n" + 5*"-" + "XOR" + 5*"-")
a = True
b = True
c = a ^ b
print(a, "and", b, "  =", c)
a = False
b = False
c = a ^ b
print(a, "and", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "and", b, " =", c)
a = False
b = True
c = a ^ b
print(a, "and", b, " =", c)

episode= 11
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Jum'at"
tanggal = 27
bulan = "Oktober"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")