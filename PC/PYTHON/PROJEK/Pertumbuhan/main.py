print("==========Pertumbuhan=========\n")

print("Masukkan nilai Pertumbuhan :\n")
mo = int(input("Masukkan Modal Awal(mo) = "))
n = int(input("Masukkan Nilai akhir tahun(n) = "))
p = int(input("berapa persen bunganya(p) = "))
p = p / 100

print('\nDiketahui :\n')
print('mo =', mo)
print('n =', n)
print('p =', p)

print("\nRumus : mn = mo ( 1 - n.p)")
print("mn =", mo, "(1 -", n, ".", p, ")")
n_p = n * p
print("mn =", mo, "( 1 -", n_p , ")")
np_1 = 1 - n_p
np_1 = float(np_1)
print("mn =", mo, "(" , np_1, ")")
mn = mo * np_1
mn = float(mn)
print("mn =", mn)
print("\n------HASILNYA DIATAS----------")