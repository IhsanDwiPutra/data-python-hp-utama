print("KALKULATOR ARITMATIKA SEDERHANA".center(60,' '),'\n',"---------------------".center(60,' '))

isLanjut = True
while isLanjut:
    nilai1 = int(input("Masukkan Angka 1 : "))
    operator = input("Masukkan Operator (+,-,x,/) : ")
    nilai2 = int(input("Masukkan Angka 2 : "))
    
    if operator == '+':
        hasil = nilai1 + nilai2
        print(nilai1, '+', nilai2,'=',hasil)
        
    elif operator == '-':
        hasil = nilai1 - nilai2
        print(nilai1,'-',nilai2,'=',hasil)
        
    elif operator == 'x' or operator == '*':
        hasil = nilai1 * nilai2
        print(nilai1,'x',nilai2,'=',hasil)
        
    elif operator == '/':
        hasil = float(nilai1) / float(nilai2)
        print(nilai1,'/',nilai2,'=',hasil)
        
    else:
        print("Ada yang Salah Nih")
        
    lanjut = input("Mau Lagi ?(y/n) : ")    
    if lanjut.lower == "n":
        isLanjut = False;