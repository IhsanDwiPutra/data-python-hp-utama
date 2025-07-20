import os

while True:
    os.system('clear')
    print(f"{'SELAMAT DATANG':^60}")
    print("DI".center(60,"-"))
    print(f"{'PROJEK COLLAB':^60}")
    print(f"{'EPS 6 - 43':^60}")
    
    
    print("\n Pilih yang mana saja :)")
    input_pilihan = int(input(f"""
  1. Casting Data {"-"*30} (Eps.6)
  2. Input User {"-"*32} (Eps.7)
  3. Operasi Aritmatika {"-"*24} (Eps.8)
  4. Konversi Temperatur {"-"*23} (Eps.9)
  5. Operasi Komparasi {"-"*25} (Eps.10)
  6. Operasi Logika / Boolean {"-"*18} (Eps.11)
  7. Latihan Komparasi & Logika {"-"*16} (Eps.12)
  8. Operator Bitwise {"-"*26} (Eps.13)
  9. Operator Assignment {"-"*23} (Eps.14)
 10. Pengenalan String {"-"*25} (Eps.15)
 11. Oprs & Manipulasi String {"-"*18} (Eps.16-17)
 12. Format String {"-"*29} (Eps.18)
 13. Width & Multiline {"-"*25} (Eps.19)
 14. Date & Time {"-"*31} (Eps.20)
 15. If & Else Statement {"-"*23} (Eps.21)
 16. Elif Statement {"-"*28} (Eps.22)
 17. Latihan Kalkulator {"-"*24} (Eps.23)
 18. For Loop / Perulangan {"-"*21} (Eps.24)
 19. While Loop {"-"*32} (Eps.25)
 20. Continue, Pass & Break {"-"*20} (Eps.26-27)
 21. Latihan Loop {"-"*30} (Eps.28)
 22. List {"-"*38} (Eps.29)
 23. Manipulasi List {"-"*27} (Eps.30)
 24. Operasi List {"-"*30} (Eps.31)
 25. Copy List {"-"*33} (Eps.32)
 26. Nested List {"-"*31} (Eps.33)
 27. Deep Copy Nested List {"-"*21} (Eps.34)
 28. Looping List & Enumerate {"-"*18} (Eps.35)
 29. Latihan List {"-"*30} (Eps.36)
 30. Tuples & Sets {"-"*29} (Eps.37)
 31. Dictionary {"-"*32} (Eps.38)
 32. Operasi Dictionary {"-"*24} (Eps.39)
 33. Looping Dictionary {"-"*24} (Eps.40)
 34. Copy & Pop Dictionary {"-"*21} (Eps.41)
 35. Multi Key & Nesting Dict {"-"*18} (Eps.42)
 36. Latihan Dictionary {"-"*24} (Eps.43)
 99. Keluar
 
 Jawaban Anda : """))
    
    if input_pilihan == 1:
        print("\n"+"1".center(60,"-"))
        print(f"{'CASTING DATA':^60}")
        print(f"{'EPS 6':^60}")
        print("Pilih salah satu ya")
        input_casting_data = int(input("""
 0. Kembali
 1. Contoh Casting Data
 9. Keluar
 
 Jawaban Anda : """))
        
        if input_casting_data == 1:
            print("\n\n")
            print(10*"=","CASTING DATA",10*"=","\n")

            print(10*"=","INTEGER",10*"=")
            data_int = 5
            print(f"Data = {data_int}\tType = {type(data_int)}")
            print("Dicasting",5*"=",">")
            data_float = float(data_int)
            data_string = str(data_int)
            data_boolean = bool(data_int)
            print(f"Data = {data_float}\tType = {type(data_float)}")
            print(f"Data = {data_string}\tType = {type(data_string)}")
            print(f"Data = {data_boolean}\tType = {type(data_boolean)}")
            
            print("\n",20*"=","\n")
            
            print(10*"=","FLOAT",10*"=")
            data_float = 5.0
            print(f"Data = {data_float}\tType = {type(data_float)}")
            print("Dicasting",5*"=",">")
            data_integer = int(data_float)
            data_string = str(data_float)
            data_boolean = bool(data_float)
            print(f"Data = {data_integer}\tType = {type(data_integer)}")
            print(f"Data = {data_string}\tType = {type(data_string)}")
            print(f"Data = {data_boolean}\tType = {type(data_boolean)}")
            
            print("\n",20*"=","\n")
            
            print(10*"=","STRING",10*"=")
            data_string = "5"
            print(f"Data = {data_string}\tType = {type(data_string)}")
            print("Dicasting",5*"=",">")
            data_integer = int(data_string)
            data_float = float(data_string)
            data_boolean = bool(data_string)
            print(f"Data = {data_integer}\tType = {type(data_integer)}")
            print(f"Data = {data_float}\tType = {type(data_float)}")
            print(f"Data = {data_boolean}\tType = {type(data_boolean)}")
            
            print("\n",20*"=","\n")
            
            print(10*"=","BOOLEAN",10*"=")
            data_boolean_1 = True
            data_boolean_2 = False
            print(f"""Data 1 = {data_boolean_1}\tType = {type(data_boolean_1)}
Data 2 = {data_boolean_2}\tType = {type(data_boolean_1)}""")
            print("Dicasting",5*"=",">")
            
            data_integer_1 = int(data_boolean_1)
            data_integer_2 = int(data_boolean_2)
            data_string_1 = str(data_boolean_1)
            data_string_2 = str(data_boolean_2)
            data_float_1 = float(data_boolean_1)
            data_float_2 = float(data_boolean_2)
            
            print(f"""Data 1 = {data_integer_1}\tType = {type(data_integer_1)}
Data 2 = {data_integer_2}\tType = {type(data_integer_1)}""")
            print(f"""Data 1 = {data_string_1}\tType = {type(data_string_1)}
Data 2 = {data_string_2}\tType = {type(data_string_1)}""")
            print(f"""Data 1 = {data_float_1}\tType = {type(data_float_1)}
Data 2 = {data_float_2}\tType = {type(data_float_1)}""")
            
            print("\nMau lanjut ?\nY. Lanjut\nN. Keluar")
            lanjut = input("Jawaban anda = ")
            if lanjut.upper() == "N":
                break
            
        elif input_casting_data == 9:
            break
            
        else: 
            print("Jawaban anda salah")
            
    elif input_pilihan == 2:
        print("\n"+"2".center(60,"-"))
        print(f"{'INPUT USER':^60}")
        print(f"{'EPS 7':^60}")
        print("Pilih salah satu ya")
        input_input_data = int(input("""
 0. Kembali
 1. Contoh Input Data
 9. Keluar
 
 Jawaban Anda : """))
        if input_input_data == 1:
            print("\n==========INPUT USER==========\n")

            nama = str(input("Masukkan nama anda : "))
            tanggal_lahir = input("Masukkan tempat tanggal lahir anda : ")
            alamat = input("Masukkan alamat anda : ")
            cita = input("Apa cita-cita anda di masa depan : ")
            no_wa = input("Minta no wa nya dong kak : ")

            print("\n\n\n\n\n\n\n\n\n\n\n\n\t\t==========BIODATA==========")
            print(f"""\t\tNAMA             : {nama}
                TEMPAT TGL LAHIR : {tanggal_lahir}
                ALAMAT           : {alamat}
                CITA-CITA        : {cita}
                NO WA            : {no_wa}
                ==========SUKSES==========

""")
            print("\nMau lanjut ?\nY. Lanjut\nN. Keluar")
            lanjut = input("Jawaban anda = ")
            if lanjut.upper() == "N":

                break
            
            elif input_input_data == 9:
                break
            
            else: 
                print("Jawaban anda salah")
                
            
    else:
        print("Masukan anda salah")
        
        
        
            
print(f"\n{'TERIMA KASIH':^60}")
print(f"{'SEMOGA HIDUP ANDA MENYENANGKAN :)':^60}")