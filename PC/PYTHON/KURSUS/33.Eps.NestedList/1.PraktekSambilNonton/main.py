# List Nested / List Bersarang

data_0 = [1.2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]

print(f"List biasa = {data_list_biasa}")

list_2d = [data_0, data_1, 6, 7]

print(f"list 2d = {list_2d}")

# contoh penggunaan

peserta_0 = ["ucucp", 25, "Laki-laki"]
peserta_1 = ["otong", 10, "Laki-laki"]
peserta_2 = ["dedeh", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f"Peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama \t: {peserta[0]}")
    print(f"Umur \t: {peserta[1]}")
    print(f"Gender \t: {peserta[2]}\n")

# dengan reference

list_copy = list_peserta.copy()
print(f"Peserta = {list_copy}")
peserta_0[0] = "michael"
print(f"Peserta = {list_copy}")
print(f"Peserta = {list_peserta}")
