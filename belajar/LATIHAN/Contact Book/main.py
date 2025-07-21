# Contact Book sederhana menggunakan python

import os

kontak = {}

def tampilkan_menu():
   os_name = os.name
   match os.name:
      case "posix": os.system("clear")
      case "nt": os.system("cls")
   
   
   print(f"\n{"SELAMAT DATANG DI":^50}")
   print(f"{"BUKU KONTAK":^50}")
   print(50*'-')
   print("1. Tampilkan Kontak")
   print("2. Tambah Kontak")
   print("3. Cari Kontak")
   print("4. Hapus Kontak")

def tambah_kontak(kontak):
   print("\n"+50*"=")
   print(f"{"TAMBAH KONTAK":^50}\n")
   nama = input("Masukan nama\t: ")
   nomor = input("Nomor\t\t: ")
   kontak[nama] = nomor
   print("Kontak berhasil ditambahkan\n")
   
   tampilkan_kontak(kontak)
   
def tampilkan_kontak(kontak):
   print("\n"+50*"=")
   print(f"{"DAFTAR KONTAK":^50}\n")
   if not kontak:
      print("Kontak masih kosong, silahkan tambahkan kontak")
   else:
      for no,data in enumerate(kontak.items()):
         print(f"{no+1}. {data[0]} - {data[1]}")

def cari_kontak(kontak):
   print("\n"+50*"=")
   print(f"{"CARI KONTAK":^50}\n")
   nama = input("Masukan nama yang ingin dicari: ")
   if nama in kontak:
      print(f"\n{nama} - {kontak[nama]}")
   else:
      print("\nKontak tidak ditemukan")

def hapus_kontak(kontak):
   print("\n"+50*"=")
   print(f"{"HAPUS KONTAK":^50}\n")
   for no,data in enumerate(kontak.items()):
         print(f"{no+1}. {data[0]} - {data[1]}")
   nama = input("\nMasukan nama yang ingin dihapus: ")
   if nama in kontak:
      del kontak[nama]
      print("\nKontak berhasil dihapus")
   else: 
      print("\nKontak tidak ditemukan")
   
# PROGRAM UTAMA KITAAAA
while(True):
   tampilkan_menu()
   
   user_option = input("\nPilih menu: ")
   
   match user_option:
      case "1": tampilkan_kontak(kontak)
      case "2": tambah_kontak(kontak)
      case "3": cari_kontak(kontak)
      case "4": hapus_kontak(kontak)
      case _: print("Menu tidak ditemukan, silahkan pilih lagi")
   
   is_done = input("\nApakah sudah selesai ? (y/n): ")
   if is_done == 'y' or is_done == 'Y':
      break






















