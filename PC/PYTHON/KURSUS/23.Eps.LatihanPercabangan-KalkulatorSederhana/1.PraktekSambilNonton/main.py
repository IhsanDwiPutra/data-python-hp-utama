# Latihan

# Latihan Percabangan - Kalkulator Sederhana
print(10*"=")
print("Kalkulator Sederhana")
print(10*"=" + "\n")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("operator (+,-,x,/) = ")
angka_2 = float(input("Masukkan angak 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("masukan yang bener dong!, aku ousying")

print("Akhir dari program, terima gaji")

