nilai1 = int(input("Masukkan angka pertama : "))
nilai2 = int(input("Masukkan angka kedua : "))

if nilai1 >= 0 or nilai2 >= 0:
    nilai1 = nilai1
    nilai2 = " + "+str(nilai2)
    print(str(nilai1)+str(nilai2))
    
else:
    nilai1 = "("+str(nilai1)+")"
    print(nilai1)