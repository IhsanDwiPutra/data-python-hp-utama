import os

inputNilai = float(input("Masukkan nilai saat ini : "))
inputTarget = float(input("Masukkan target nilai: "))
hasil = (inputNilai / inputTarget) * 100
os.system('clear')
print(f"Hasilnya adalah {int(hasil)}%")

progres = 100
print(progres*"•")