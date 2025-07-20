while True:
    print("Operasi dan Manipulasi String".center(40, "-"))

    print("\n"+"Welcome".center(40))
    user_input = input("Pilihlah untuk melihat lebih detail :\n1. Merubah case dari string\n2. Pengecekan dengan isX\n3. Mengecek komponen awal dan akhir\n4. Penggabungan komponen\n5. Alokasi karakter\nPilihan anda (q untuk keluar): ")

    if user_input == "1":
        print("\n"+"1. MERUBAH CASE DARI STRING".center(40, "="))

        input_case = input("Yang mana :\na. Lower Case\nb. Upper Case\nJawaban anda : ")
        if input_case == "a":
           print("\na. Lower Case (lower())")
           data_input = input("\nMasukkan string yang ingin di ubah : ")
           print("\nJawaban anda : " + str(data_input))
           lower = data_input.lower()
           print("Jadinya : "+ lower)
        
      elif input_case == "b":
           print("\n"+"2. PENGECEKAN DENGAN ISx".center(40, "="))
           print("\na. Lower Case (lower())")
           data_input = input("\nMasukkan string yang ingin di ubah : ")
           print("\nJawaban anda : " + str(data_input))
           lower = data_input.lower()
           print("Jadinya : "+ lower)
        
      else:
           print("\nJawaban anda salah, pilihan hanya 1 - 5")

           ulang = input("\nApakah Anda ingin melakukan operasi lainnya? (y/n): ")
            if ulang.lower() != 'y':
                break
