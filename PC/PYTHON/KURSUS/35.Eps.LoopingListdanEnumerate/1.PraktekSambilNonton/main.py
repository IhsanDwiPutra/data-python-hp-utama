# Looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4, 2, 5, 6, 1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")


peserta = ["ucup", "dadang", "diding", "dudung"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFor Loop dan Range")
kumpulan_angka = [10, 5, 4, 2, 6]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("\nWhile Loop")
kumpulan_angka = [10, 5, 4, 2, 6]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1


# list comphrension
print("\nList Comprehension")
data = ["ucup", 1, 2, 3, "otong"]

[print(f"data={i}") for i in data]

kumpulan_angka = [10, 5, 4, 2, 6]

angka_kuadrat = [i**2 for i in kumpulan_angka]
print(angka_kuadrat)

# enumerate
print("\nEnumerate")
data_list = ["ucup", 1, 2, 3, "otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
