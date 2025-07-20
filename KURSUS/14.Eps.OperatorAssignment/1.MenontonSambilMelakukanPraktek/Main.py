print(20*"=" + "OPERATOR ASSIGNMENT" + 20*"=")
# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

# adalah assignment
# operasi aritamtika
a = 5 
print("\nnilai a =", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1 menjadi =", a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2 menjadi =", a)

a *= 5
print("nilai a *= 5 menjadi =", a)

a /= 2
print("nilai a /= 2 menjadi =", a)


# modulus dan floor division
b = 10
print("\nnilai b adalah =", b)

b %= 3
print("nilai b %= 3 menjadi =", b)

b = 10
print("\nnilai b adalah =", b)

b //= 3
print("nilai b //= 3 menjadi =", b)


# pangkat atau eksponen
a = 5
print(" nilai a adalah =", a)
a **= 3
print("nilai a **= 3 adalah =", a)

#operasi bitwise
# OR
c = True
print("\nnilai c adalah =",c)
c |= False
print("nilai c |= False menjadi =", c)
c = False
print("\nnilai c adalah =",c)
c |= False
print("nilai c |= False menjadi =", c)

# AND
c = True
print("\nnilai c adalah =",c)
c &= False
print("nilai c &= False menjadi =", c)
c = True
print("\nnilai c adalah =",c)
c &= True
print("nilai c &= True menjadi =", c)


# XOR
c = True
print("\nnilai c adalah =",c)
c ^= False
print("nilai c ^= False menjadi =", c)
c = False
print("\nnilai c adalah =",c)
c ^= False
print("nilai c ^= False menjadi =", c)


# geser - geser
d = 0b0100
print("nilai d =",format(d,"04b"))
d >>= 2
print("nilai d >>= 2 menjadi =",format(d,"04b"))
d <<= 1
print("nilai d <<= 1 menjadi =",format(d,"04b"))