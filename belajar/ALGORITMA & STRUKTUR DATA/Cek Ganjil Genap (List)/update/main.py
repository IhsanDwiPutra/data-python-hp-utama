# PROGRAM CEK GANJIL GENAP

print(f"{'CEK GANJIL GENAP':^50}") 
print(50*'='+"\n")

angka_list = []

jumlah = int(input("Banyak angka yang ingin dicek: "))

for i in range(jumlah):
   angka = int(input(f"{i+1}. Masukan angka: "))
   angka_list.append(angka)

print(50*'-')

for no,angka in enumerate(angka_list):
   if angka % 2 == 0:
      print(f"{no+1}. {angka} adalah bilangan GENAP")
   else:
      print(f"{no+1}. {angka} adalah bilangan GANJIL")












