# Buku Kontak Sederhana | update 3 - json

import os
import json

# Fungsi Utilitas

def clear_screen():
   match os.name:
      case "posix": os.system("clear")
      case "nt": os.system("cls")

def input_nomor(prompt):
   while True:
      nomor = input(prompt)
      if len(nomor) != 12:
         print("\nNomor harus 12 digit")
         continue
      elif nomor[0:2] != '08':
         print("\nAwalan harus sesuai format (cnth:081234567890)")
         continue
      else: 
         return nomor

# Fungsi Simpan & Muat json

def simpan_kontak(kontak, nama_file="kontak.json"):
   with open(nama_file, 'w') as file:
      json.dump(kontak, file)

def muat_kontak(nama_file="kontak.json"):
   try:
      with open(nama_file, 'r') as file:
         return json.load(file)
   except FileNotFoundError:
      return {}

# Fungsi Menu

def lihat_kontak(kontak):
   clear_screen()
   
   print(f"{'DAFTAR KONTAK':^50}")
   print(f"{'------------------':^50}\n")
   
   if not kontak:
      print(f"{'--Kontak Masih Kosong--':^50}")
   else:
      print(50*'-')
      print(f"{'NO':^4} | {'NAMA':<20} | {'NOMOR':<15}")
      print(50*'-')
      for no, data in enumerate(kontak.items()):
         print(f"{no+1:^4} | {data[0].title():<20} | {data[1]:<15}")
      print(50*'-')
      
   input("\nKembali ke Menu...").strip().lower()
   
   

def tambah_kontak(kontak):
   while True:
      clear_screen()
      
      print(f"{'TAMBAH KONTAK':^50}")
      print(f"{'------------------':^50}\n")
      
      nama = input("Nama\t\t\t : ").lower()
      nomor = input_nomor("Nomor (cth:081234567890) : ")
      
      if nama in kontak:
         print(f"\n{'-- X Kontak Sudah ada --':^50}")
      else:
         kontak[nama] = nomor
         simpan_kontak(kontak)
         print("\nKontak berhasil ditambahkan")
      if input("\nTambahkan lagi ? (y/n): ").lower() == 'n': break

def hapus_kontak(kontak):
   while True:
      clear_screen()
         
      print(f"{'HAPUS KONTAK':^50}")
      print(f"{'------------------':^50}\n")
         
      nama = input("Nama kontak yang ingin dihapus: ").lower()
      
      if nama in kontak:
         del kontak[nama]
         simpan_kontak(kontak)
         print("\nKontak Berhasil dihapus")
      else:
         print("\nKontak tidak ditemukan")
      if input("\nHapus lagi ? (y/n): ").lower() == 'n': break

def cari_kontak(kontak):
   while True:
      clear_screen()
      
      print(f"{'CARI KONTAK':^50}")
      print(f"{'------------------':^50}\n")
         
      nama = input("Nama kontak yang ingin dicari: ").lower()
      
      if nama in kontak:
         print(f"\n{'-- KONTAK DITEMUKAN --':^50}")
         print(f"\n\tNama\t: {nama.title()}")
         print(f"\tNomor\t: {kontak[nama]}")
      else:
         print(f"\n{'-- KONTAK TIDAK DITEMUKAN --':^50}")
         
      if input("\nCari kontak lagi ? (y/n): ").lower() == 'n': break

def ubah_kontak(kontak):
   while True:
      clear_screen()
      
      print(f"{'UBAH KONTAK':^50}")
      print(f"{'------------------':^50}\n")
         
      nama = input("Nama kontak yang ingin diubah: ").lower()
      
      if nama in kontak:
         print(f"\n{'-- KONTAK DITEMUKAN --':^50}")
         print(f"\n\tNama\t: {nama.title()}")
         print(f"\tNomor\t: {kontak[nama]}")
         
         print("\nData mana yang ingin di ubah")
         print("1. Nama")
         print("2. Nomor")
         user_option = input("Pilihan Anda: ").lower()
         
         if user_option == '1':
            nama_baru = input("\nMasukan nama baru: ").lower()
            kontak[nama_baru] = kontak.pop(nama)
            simpan_kontak(kontak)
            print("\nNama berhasil di update!")
         elif user_option == '2':
            nomor_baru = input_nomor("\nMasukan nomor baru: ")
            kontak[nama] = nomor_baru
            simpan_kontak(kontak)
            print("\nNomor berhasil di update!")
         else:
            print("\nPilihan tidak ditemukan!")
      
      else:
         print(f"\n{'-- KONTAK TIDAK DITEMUKAN --':^50}")
      
      if input("\nUbah kontak lagi ? (y/n): ").lower() == 'n': break

# Program utama

data_kontak = muat_kontak()

while True:
   clear_screen()
   print(f"{'Buku Kontak Sederhana':^50}")
   print(50*'=')
   print("""
   1. Lihat Kontak
   2. Tambah Kontak 
   3. Hapus Kontak 
   4. Cari Kontak
   5. Ubah Kontak
   6. Keluar
   """)
   
   user_option = input("   Pilihan Anda: ")
   
   match user_option:
      case "1": lihat_kontak(data_kontak)
      case "2": tambah_kontak(data_kontak)
      case "3": hapus_kontak(data_kontak)
      case "4": cari_kontak(data_kontak)
      case "5": ubah_kontak(data_kontak)
      case "6": break
      case _: input("\n   Pilihan Anda tidak ditemukan, Coba Lagi...").strip().lower()

print("\n   Terima kasih telah berkunjung :)")