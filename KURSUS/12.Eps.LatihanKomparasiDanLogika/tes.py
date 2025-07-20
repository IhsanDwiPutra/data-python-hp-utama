inputUser = int(input("Masukkan diatas 5 dan di bawah 10 : "))
isKurangDari = (5 < inputUser)
print(inputUser,'< 5 =', isKurangDari)
isLebihDari = (10 > inputUser)
print(inputUser,'> 10 =',isLebihDari)
isTrue = isKurangDari and isLebihDari
print(isTrue)
