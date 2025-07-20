print("=====Bunga Majemuk====")
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
print("Rumus : mn = mo ( 1 + b) n(pangkat)")
print("mn =", mo, "(1 +", b, ")", n, "pangkat")
b_1 = 1 + b
print("mn =", mo, "(", b_1, ")", n, "pangkat")
b_pangkatn = b_1 ** n
b_pangkatn = float(b_pangkatn)
print("mn =", mo, "(" , b_pangkatn, ")")
mn = mo * b_pangkatn
mn = float(mn)
print("mn =", mn)
print("------HASILNYA DIATAS----------")