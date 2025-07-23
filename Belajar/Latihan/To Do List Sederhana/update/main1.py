# Program To Do List 

import os

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear")

def tampilkan_tugas(tugas):
   print(f"{'TO DO LIST':^50}")
   print(50*'-'+'\n')
   if not tugas:
      print(f"{'-- Belum ada tugas --':^50}")
   else:
      for i, item in enumerate(tugas, start=1):
         print(f"{i}. {item.title()}")
   print("\n"+50*'-')

def tambah_tugas(tugas):
   item = input("\nMasukan nama tugas: ").lower()
   if item in tugas:
      input("\nTugas sudah ada...[Enter]").strip()
   else:
      tugas.append(item)
      input("Tugas berhasil ditambahkan...[Enter]").strip()

def hapus_tugas(tugas):
   tampilkan_tugas(tugas)
   try:
      index = int(input("Nomor tugas yang akan dihapus: "))
      if 1 <= index <= len(tugas):
         tugas.pop(index-1)
         input("Tugas berhasil dihapus...[Enter]").strip()
      else: input("Nomor tidak valid...[Enter]").strip()
   except ValueError: 
      input("Masukan angka yang valid...[Enter]").strip

def bersihkan_tugas(tugas):
   tugas.clear()
   input("Semua tugas telah dihapus...[Enter]").strip()

def menu():
   tugas = []
   while True:
      clear_screen()
      tampilkan_tugas(tugas)
      print("""
1. Tambah Tugas
2. Hapus Tugas
3. Bersihkan Semua Tugas
4. Keluar""")
      pilihan = input("Pilih menu: ")
      
      match pilihan:
         case "1": tambah_tugas(tugas)
         case "2": hapus_tugas(tugas)
         case "3": bersihkan_tugas(tugas)
         case "4": break
         case _: input("Pilihan tidak valid... [Enter]").strip().lower()

menu()
print("\nTerima kasih telah berkunjung orang :)")