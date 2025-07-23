# PROGRAM DAFTAR BELANJA

import os 

def clear_screen():
   match os.name:
      case "posix": os.system("clear")
      case "nt": os.system("cls")


def tampilkan_daftar(list_belanja):
   while True:
      print("\n"+50*'-')
      print(f"{'DAFTAR BELANJAAN':^50}")
      print(50*'-'+'\n')
      if not list_belanja:
         print(f"{'Barang masih kosong':^50}\n")
      else:
         for no,item in enumerate(list_belanja):
            print(f"{no+1}. {item}")
      
      is_tambah = input("Tambahkan barang? (y/n): ").lower()
      if is_tambah != 'y':
         return
      else:
         tambah_belanja(list_belanja)

def tambah_belanja(list_belanja):
   
   item = input("Barang yang ingin ditambahkan: ")
   if item in list_belanja:
      print("Barang sudah ada")
   else:
      daftar_belanja.append(item)

def hapus_belanja(list_belanja):
   item = input("Barang yang ingin dihapus: ")
   if item in list_belanja:
      list_belanja.remove(item)
      print(f"{item} berhasil dihapus")
   else:
      print("Barang tidak ditemukan")


daftar_belanja = []

while True:
   clear_screen()
   
   print(f"{'DAFTAR BELANJA':^50}")
   print(50*'-'+'\n')
   
   print("1. Lihat Daftar Belanja")
   print("2. Tambah Belanjan")
   print("3. Hapus Belanja")
   print("4. Keluar")
   
   user_option = input("\nPilihan Anda: ")
   
   match user_option:
      case '1': tampilkan_daftar(daftar_belanja)
      case '2': tambah_belanja(daftar_belanja)
      case '3': hapus_belanja(daftar_belanja)
      
   is_done = input("Apakah selesai? (y/n): ").lower()
   if is_done != 'y':
      print("Terima kasih telah berkunjung :)")
      break

   












