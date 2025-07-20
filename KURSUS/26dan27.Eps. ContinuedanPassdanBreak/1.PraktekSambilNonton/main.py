# Continue dan Pass dan Break


# Pass > dia berfungsi sebagai dummy, tidak akan dieksekusi
print("1. Pass dibawah ini")
angka = 0

while angka < 5:
    
    angka += 1
    if angka == 3:
        pass # ini tidak akan dieksekusi
        
    print(angka)
    
# continue
print("\n2. Continue")

angka = 0
print(f"angka sekarang adalah {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang adalah {angka}")
    if angka == 3:
        print("nice")
        continue
    
    print("washhupppp")
    
print("mantappp")

# Break
print("\n3. Break")

angka = 0

while angka < 5:
    angka += 1
    print(f"Angka sekarang adalah {angka}")
    
    if angka == 3 :
        print("nice!!!!")
        break
        
    print("wassshuppp")
    
print("cukup finishhhh")

input = int(input("Masukkan hitung sampai berapa = "))
angka = 0

while True:
    angka += 1
    print(f"Hitung = {angka}")
    
    if angka == input :
        print("nice!!!!")
        break
        
    print("wassshuppp")
    
print("cukup finishhhh")