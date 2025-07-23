# PROGRAM DAFTAR BELANJA

import os 

def clear_screen():
   os.system("clear" if os.name == "posix" else "cls")

def is_done(prompt):
   while True:
      is_tambah = input(prompt).strip().lower()
      if not is_tambah:
         input("❌ Masukan tidak boleh kosong...")
         continue
      elif is_tambah == 'n':
         return False
      elif is_tambah == 'y': 
         return True
      else: 
         input("Pilihan tidak ditemukan...")
         continue

def tampilkan_barang(list_belanja):
   for no, barang in enumerate(list_belanja,start=1):
         print(f"{no}. {barang.title()}")

def tampilkan_daftar(list_belanja):
   clear_screen()
   print(f"{'DAFTAR BELANJAAN':^50}")
   print(50*'-'+'\n')
   
   if not list_belanja:
      print(f"{'- Barang Masih Kosong -':^50}")
   else:
      tampilkan_barang(list_belanja)
   input("\nTekan Enter untuk kembali ke menu...")

def tambah_belanja(list_belanja):
   is_lanjut = True
   while is_lanjut:
      item = input("\nBarang yang ingin ditambahkan: ").strip().lower()
      if not item:
         print("❌ Nama barang tidak boleh kosong")
      elif item in list_belanja:
         print("❌  Barang sudah ada di daftar belanjaan")
      else:
         list_belanja.append(item)
         print("✔️  Barang berhasil ditambahkan")
      
      is_lanjut = is_done("\nTambahkan barang lagi? (y/n): ")

def hapus_belanja(list_belanja):
   is_lanjut = True
   while is_lanjut:
      barang = input("\nMasukkan barang yang ingin dihapus: ").strip().lower()
      if not barang:
         input("❌ Nama barang tidak boleh kosong...")
      elif barang in list_belanja:
         list_belanja.remove(barang)
         print("✔️ Barang berhasil dihapus")
      else:
         print("❌ Barang tidak ditemukan")
      is_lanjut = is_done("\nHapus barang lagi? (y/n): ")

def bersihkan_belanja(list_belanja):
   while True:
      if not list_belanja:
         input("\nBelanjaan sudah kosong...")
         break
      is_clear = input("\nYakin membersihkan belanja? (y/n): ").lower().strip()
      if not is_clear:
         input("\n❌ Pilihan tidak boleh kosong...")
         continue
      elif is_clear == 'y':
         list_belanja.clear()
         input("\n✔️ Belanjaan berhasil di bersihkan...")
         break
      elif is_clear == 'n':
         input("\nPembersihan di batalkan...")
         break 
      else:
         input("\nPilihan tidak ditemukan...")

def edit_belanja(list_belanja):
   if not list_belanja:
      input("\nBelanjaan kosong...")
      return
   print("\n- Daftar Belanjaan:")
   tampilkan_barang(list_belanja)
   print(50*'-')
   barang_lama = input("Nama barang yang ingin diubah: ").strip().lower()
   if not barang_lama:
      input("\n❌ Nama barang tidak boleh kosong...")
      return
   elif barang_lama in list_belanja:
      barang_baru = input("\nNama baru: ").strip().lower()
      if not barang_baru:
         input("❌ Nama barang tidak boleh kosong...")
         return
      elif barang_baru in list_belanja:
         input("❌ Barang sudah ada di daftar, tidak bisa duplikat...")
         return
      else:
         index = list_belanja.index(barang_lama)
         list_belanja[index] = barang_baru
         input("✔️ Nama barang berhasil diubah...")
         return
   else:
      input("\nBarang tidak ditemukan...")
      return

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
      print("5. Edit Belanjaan")
      print("6. Keluar")
      user_option = input("\nPilihan: ").strip()
      if not user_option:
         input("\n❌ Pilihan tidak boleh kosong...")
         continue
      match user_option:
         case '1': tampilkan_daftar(daftar_belanja)
         case '2': tambah_belanja(daftar_belanja)
         case '3': hapus_belanja(daftar_belanja)
         case '4': bersihkan_belanja(daftar_belanja) 
         case '5': edit_belanja(daftar_belanja)
         case '6': break 
         case _: 
            print("\nPilihan tidak ditemukan")
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
   main()
   print("\nTerima Kasih telah berkunjung :)")