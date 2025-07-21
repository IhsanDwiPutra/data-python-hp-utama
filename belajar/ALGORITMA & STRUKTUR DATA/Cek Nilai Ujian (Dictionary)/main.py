# PROGRAM Cek Nilai Ujian

import os 

def clear_screen():
   match os.name:
      case "posix": os.system("clear")
      case "nt": os.system("cls")

def input_angka(prompt):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         print("❌   Input harus angka, Coba Lagi\n")

def main():
   clear_screen()
   
   print(f"{'PROGRAM CEK NILAI UJIAN':^50}")
   print(50*'='+'\n')
   
   data_siswa = {}
   jumlah = input_angka("Berapa banyak siswa: ")
   
   print("\nINPUT DATA -----")
   for i in range(jumlah):
      nama = input(f"Nama siswa ke-{i+1}\t: ")
      nilai = input_angka("Nilai siswa\t: ")
      data_siswa[nama] = nilai
   
   print("\n"+50*'-')
   lulus = []
   tidak_lulus = []
   
   print(f"{'NO':3}| {'NAMA':30}| {"STATUS":10}")
   print(50*'-')
   for no,data in enumerate(data_siswa.items()):
      nama = data[0]
      nilai = data[1]
      status = "LULUS" if nilai >= 75 else "TIDAK LULUS"
      print(f"{no+1:^3}| {nama.title():30}| {status:^10}")
      
      if status == "LULUS":
         lulus.append(nama)
      else:
         tidak_lulus.append(nama)
   print(50*'-'+"\n")
   
   print("Summary")
   print(f"- Total siswa LULUS: {len(lulus)} -> {lulus}")
   print(f"- Total siswa TIDAK LULUS: {len(tidak_lulus)} -> {tidak_lulus}")

# PROGRAM UTAMA
while True:
   main()
   
   is_done = input("\nCek lagi? (y/n): ").lower()
   if is_done != 'y':
      print("Terima kasih sudah berkunjung, tetap semangat 💪")
      break









