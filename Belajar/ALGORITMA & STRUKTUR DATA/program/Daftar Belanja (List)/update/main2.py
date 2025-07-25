# PROGRAM DAFTAR BELANJA

import os 

def clear_screen():
   os.system("clear" if os.name == "posix" else "cls")

def tampilkan_daftar(list_belanja):
   clear_screen()
   print(f"{'DAFTAR BELANJAAN':^50}")
   print(50*'-'+'\n')
   
   if not list_belanja:
      print(f"{'- Barang Masih Kosong -':^50}")
   else:
      for no, barang in enumerate(list_belanja,start=1):
         print(f"{no}. {barang.title()}")
   input("\nTekan Enter untuk kembali ke menu...")

def tambah_belanja(list_belanja):
   while True:
      item = input("\nBarang yang ingin ditambahkan: ").lower()
      if item in list_belanja:
         print("❌  Barang sudah ada di daftar belanjaan")
      else:
         list_belanja.append(item)
         print("✔️  Barang berhasil ditambahkan")
      
      if input("\nTambahkan lagi? (y/n): ").lower() == 'n': break

def hapus_belanja(list_belanja):
   while True:
      barang = input("\nMasukkan barang yang ingin dihapus: ").lower()
      if barang in list_belanja:
         list_belanja.remove(barang)
         print("✔️ Barang berhasil dihapus")
      else:
         print("❌ Barang tidak ditemukan")
      if input("\nHapus barang lagi? (y/n): ").lower() == 'n': break

def bersihkan_belanja(list_belanja):
   list_belanja.clear()
   input("✔️ Belanja berhasil dibersihkan...")

def main():
   daftar_belanja = []
   while True:
      clear_screen()
      print(f"{'PROGRAM DAFTAR BELANJA':^50}")
      print(50*'-'+'\n')
      print("1. Lihat Daftar Belanja")
      print("2. Tambah Belanja")
      print("3. Hapus Belanja")
      print("4. Bersihkan Belanjaan")
      print("5. Keluar")
      user_option = input("\nPilihan: ")
      match user_option:
         case '1': tampilkan_daftar(daftar_belanja)
         case '2': tambah_belanja(daftar_belanja)
         case '3': hapus_belanja(daftar_belanja)
         case '4': bersihkan_belanja(daftar_belanja) 
         case '5': break 
         case _: 
            print("\nPilihan tidak ditemukan")
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
   main()
   print("\nTerima Kasih telah berkunjung :)")