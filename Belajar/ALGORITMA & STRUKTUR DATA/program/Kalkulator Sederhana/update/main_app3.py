# Kalkulator Sederhana update 3

import os 
import math

def clear_screen():
   match os.name:
      case "posix": os.system("clear")
      case "nt": os.system("cls")

def input_float(prompt):
   while True:
      try:
         return float(input(prompt))
      except ValueError:
         print("❌  Input harus angka, Coba Lagi\n")

def loop_operasi(nama, operasi, is_binary=True):
   while True:
      clear_screen()
      print(f"{nama:^50}")
      print(50*'-'+'\n')
      
      angka1 = input_float("Angka Pertama\t: ")
      angka2 = input_float("Angka Kedua\t: ") if is_binary else None 
      
      hasil = operasi(angka1, angka2) if is_binary else operasi(angka1)
      
      print('\n'+50*'-')
      operator = operasi.__name__.replace('_',' ')
      print(f"Hasil: {hasil}")
      print(50*'-'+'\n')
      
      if input("Lanjut Operasi ini (y/n): ").lower() == 'y': break
      

def operasi_tambah():
   loop_operasi("OPERASI TAMBAH", lambda a,b: a + b)

def operasi_kurang():
   loop_operasi("OPERASI KURANG", lambda a,b: a - b)

def operasi_kali():
   loop_operasi("OPERASI KALI", lambda a,b: a * b)

def operasi_bagi():
   def bagi(a,b):
      return "❌  Error (dibagi 0)" if b == 0 else a / b
   loop_operasi("OPERASI BAGI", bagi)

def operasi_sisa_pembagian():
   def sisa(a,b):
      return "❌  Error (dibagi 0)" if b == 0 else a % b
   loop_operasi("OPERASI SISA PEMBAGIAN", sisa)

def operasi_membulatkan():
   def bulatkan(a,b):
      return "❌  Error (dibagi 0)" if b == 0 else a // b
   loop_operasi("OPERASI PEMBULATAN", bulatkan)

def operasi_pangkat():
   loop_operasi("OPERASI PANGKAT", lambda a,b: a ** b)

def operasi_akar():
   loop_operasi("OPERASI AKAR", lambda a: math.sqrt(a), is_binary=False)

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
   8. Operasi Akar 
   9. Keluar
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
      case '8': operasi_akar()
      case '9': break
      case _: input("\n❌  Pilihan Anda tidak ditemukan coba lagi...")

print("\nTerima Kasih telah berkunjung :)")