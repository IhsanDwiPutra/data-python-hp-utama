# Kalkulator Sederhana

import os 

def clear_screen():
   match os.name:
      case "posix": os.system("clear")
      case "nt": os.system("cls")

def input_float(prompt):
   while True:
      try:
         return float(input(prompt))
         break
      except ValueError:
         print("❌  Input harus angka, Coba Lagi\n")

def operasi_tambah():
   while True:
      clear_screen()
      
      print(f"{'OPERASI TAMBAH':^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama\t: ")
      angka2 = input_float("Angka Kedua\t: ")
      
      hasil = angka1 + angka2
      print('\n'+50*'-')
      print(f"{angka1:,} + {angka2} = {hasil:,}")
      print(50*'-'+'\n')
      
      is_done = input("Apakah sudah selesai? (y/n): ").lower()
      if is_done == 'y':
         break

def operasi_kurang():
   while True:
      clear_screen()
      
      print(f"{'OPERASI KURANG':^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama: ")
      angka2 = input_float("Angka Kedua: ")
      
      hasil = angka1 - angka2
      print('\n'+50*'-')
      print(f"{angka1} - {angka2} = {hasil:,}")
      print(50*'-'+'\n')
      
      is_done = input("Apakah sudah selesai? (y/n): ").lower()
      if is_done == 'y':
         break

def operasi_kali():
   while True:
      clear_screen()
      
      print(f"{'OPERASI KALI':^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama\t: ")
      angka2 = input_float("Angka Kedua\t: ")
      
      hasil = angka1 * angka2
      print('\n'+50*'-')
      print(f"{angka1:,} * {angka2} = {hasil:,}")
      print(50*'-'+'\n')
      
      is_done = input("Apakah sudah selesai? (y/n): ").lower()
      if is_done == 'y':
         break

def operasi_bagi():
   while True:
      clear_screen()
      
      print(f"{'OPERASI BAGI':^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama\t: ")
      angka2 = input_float("Angka Kedua\t: ")
      
      if angka2 == 0:
         input("\nTidak boleh dibagi dengan '0' ...")
         continue
      else:
         hasil = angka1 / angka2
         print('\n'+50*'-')
         print(f"{angka1:,} / {angka2} = {hasil:,}")
         print(50*'-'+'\n')
         
         is_done = input("Apakah sudah selesai? (y/n): ").lower()
         if is_done == 'y':
            break

def operasi_sisa_pembagian():
   while True:
      clear_screen()
      
      print(f"{'OPERASI SISA PEMBAGIAN':^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama\t: ")
      angka2 = input_float("Angka Kedua\t: ")
      
      hasil = angka1 % angka2
      print('\n'+50*'-')
      print(f"{angka1:,} % {angka2} = {hasil:,}")
      print(50*'-'+'\n')
      
      is_done = input("Apakah sudah selesai? (y/n): ").lower()
      if is_done == 'y':
         break

def operasi_membulatkan():
   while True:
      
      clear_screen()
      
      print(f"{'OPERASI PEMBULATAN':^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama\t: ")
      angka2 = input_float("Angka Kedua\t: ")
      
      hasil = angka1 // angka2
      print('\n'+50*'-')
      print(f"{angka1:,} // {angka2} = {hasil:,}")
      print(50*'-'+'\n')
      
      is_done = input("Apakah sudah selesai? (y/n): ").lower()
      if is_done == 'y':
         break

def operasi_pangkat():
   while True:
      clear_screen()
      
      print(f"{'OPERASI PANGKAT':^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama\t: ")
      pangkat = input_float("Di pangkat\t: ")
      
      hasil = angka1 ** pangkat
      print('\n'+50*'-')
      print(f"{angka1} ** {pangkat} = {hasil:,}")
      print(50*'-'+'\n')
      
      is_done = input("Apakah sudah selesai? (y/n): ").lower()
      if is_done == 'y':
         break

while True:
   clear_screen()
   
   print(f"{'KALKULATOR SEDERHANA':^50}")
   print(50*'=')
   
   print("""
   1. Operasi +
   2. Operasi -
   3. Operasi x 
   4. Operasi /
   5. Operasi % (Sisa Pembagian)
   6. Operasi // (Membulatkan)
   7. Operasi ** (Pangkat)
   8. Keluar
   """)
   
   user_option = input("Pilih Operasi: ")
   
   match user_option:
      case '1': operasi_tambah()
      case '2': operasi_kurang()
      case '3': operasi_kali()
      case '4': operasi_bagi()
      case '5': operasi_sisa_pembagian()
      case '6': operasi_membulatkan()
      case '7': operasi_pangkat()
      case '8': break
      case _: input("\n❌  Pilihan Anda tidak ditemukan coba lagi...")

print("\nTerima Kasih telah berkunjung :)")