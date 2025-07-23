import random

angka_rahasia = random.randint(1, 240000)
tebakan = 0
jumlah_tebakan = 0

while tebakan != angka_rahasia:
   try:
      tebakan = int(input("Masukan tebakan Anda: "))
      jumlah_tebakan +=1
      
      if tebakan > angka_rahasia:
         print("Tebakan Anda tinggi")
      elif tebakan < angka_rahasia:
         print("Tebakan Anda rendah")
   except ValueError:
      print("❌   Input harus angka")

print(f"Selamat tebakan Anda benar yaitu {angka_rahasia}, jumlah tebakan = {jumlah_tebakan}")