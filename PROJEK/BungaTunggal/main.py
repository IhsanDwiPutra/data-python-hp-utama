print("=====Bunga Tunggal====")
print("===================")
print("Diketahui :")
mo = int(input("Masukkan Modal Awal(mo) = "))
n = int(input("Masukkan Suku n(n) = "))
b = int(input("berapa persen bunganya(b) = "))
b = b / 100
print("===================")
print('Diketahui :')
print('mo =', mo)
print('n =', n)
print('b =', b)

print("===================")
print(f"Rumus : mn = mo(1+n.b)")
print("mn =", mo, "(1 +", n, "x", b, ")")
n_b = n * b
print("mn =", mo, "(1 +", n_b, ")")
n_b1 = 1 + n_b
print("mn =", mo, "(" , n_b1, ")")
mn = mo * n_b1
mn = int(mn)
print("mn =", mn)
print("------HASILNYA DIATAS----------")