print(20*"=" + "OPERATOR ASSIGNMENT" + 20*"=")


print("--OPERASI ARITMATIKA--")
a = 10
print("\nNilai a =",a)

a += 5
print("\nNilai a += 5 =",a)

a -= 3
print("Nilai a -= 3 =",a)

a *= 2
print("Nilai a *= 2 =",a)

a /= 2
print("Nilai a /= 6 =",a)


print("\n--MODULUS--")
b = 13
print("\nNilai b =",b)

b %= 2
print("\nNilai b %= 2 =",b)

print("--FLOOR DIVISION--")
b = 13
print("\nNilai b =",b)

b //= 3
print("\nNilai b //= 3 =",b)

print("--OPERASI BITWISE--\n-OR-")
c = True
print("\nNilai c =",c)

c |= False
print("\nNilai c |= False =",c)

c = False
print("Nilai c =",c)

c |= False
print("Nilai c |= False =",c)

print("\n-AND-")
d = True
print("\nNilai d =",d)

d &= True
print("\nNilai d &= True =",d)

d = True
print("Nilai d =",d)

d &= False
print("Nilai d &= False =",d)

print("\n-XOR-")
e = True
print("\nNilai e =",e)

e ^= False
print("\nNilai e^= False =",e)

e = True
print("Nilai e =",e)

e ^= True
print("Nilai e ^= True =",e)


print("\n--GESER - GESER--\n-GESER KE KANAN-\n")

f = 0b0101
print("Nilai f =",format(f,"04b"))

f >>= 2
print("\nNilai f >>= 2 =",format(f,"04b"))

print("-GESER KE KIRI-\n")
f = 0b0001
print("Nilai f =",format(f,"04b"))

f <<= 2
print("\nNilai f <<= 2 =",format(f,"04b"))

episode = 14
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Kamis"
tanggal = 9
bulan = "November"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")