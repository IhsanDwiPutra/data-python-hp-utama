# Latihan Loop


sisi = 5
print("1. Menggunakan For")

count = 1
for i in range(sisi):
    print("+"*count)
    count += 1
    
print("Akhir dari For\n")

print("2. Menggunakan While")

count = 1
while True:
    print("+"*count)
    count += 1
    
    if count > sisi :
        break
        
print("Akhir While\n")

print("3. Hanya ganjil")

count = 1
while True:
    
    if count % 2:
        print("+"*count)
        count += 1
        
    else :
        count += 1
        continue
        
    if count > sisi:
        break
        
print("Akhir dari ganjil\n")

print("5. Membuat segitiga sama kaki")

sisi = 7
count = 1
spasi = int(sisi / 2)

while True:
    if count % 2 :
        print(" "*spasi+"+"*count)
        spasi -= 1
        count += 1
        
    else:
        count += 1
        continue
        
    if count > sisi:
        break
        
# Bagian bawah
count = sisi - 2
spasi = 1

while True:
    if count % 2:
        print(" "*spasi+"+"*count)
        spasi += 1
        count -= 1
        
    else:
        count -= 1
        continue
        
    if count <= 0:
        break