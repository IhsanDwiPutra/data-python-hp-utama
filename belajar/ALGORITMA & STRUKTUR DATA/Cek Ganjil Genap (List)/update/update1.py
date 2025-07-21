# PROGRAM CEK GANJIL GENAP update 1

import os

def clear_screen():
   name = os.name
   match name:
      case 'posix': os.system("clear")
      case 'nt': os.system("cls")

def input_angka(prompt):
   while True:
      try:
         return int(input(prompt))
      except:
         print("❌  input harus angka. Coba Lagi\n")

def cek_ganjil_genap(angka):
   return "GENAP" if angka % 2 == 0 else "GANJIL"

def main():
   clear_screen()
   
   print(f"{'CEK GANJIL GENAP':^50}") 
   print(50*'='+"\n")
   
   angka_list = []
   jumlah = input_angka("Banyak angka yang ingin dicek: ")
   
   for i in range(jumlah):
      angka = input_angka(f"{i+1}. Masukan angka: ")
      angka_list.append(angka)
   
   print('\n'+50*'-'+'\n')
   
   for no,angka in enumerate(angka_list):
      hasil = cek_ganjil_genap(angka)
      print(f"{no+1}. {angka} adalah bilangan {hasil}")

# PROGRAM UTAMA
while(True):
   main()
   
   is_done = input("\nIngin cek lagi? (y/n): ").lower()
   if is_done != 'y':
      print("\nTerima kasih telah menggunakan program ini, semoga hari anda menyenangkan")
      break












