# Perulangan (loop)

# for kondisi:
#     aksi

# ini dengan list
# angka_list = [0, 1, 2, 3, 4]
# print(angka_list)

# for i in angka_list:
#     print(f"i sekarang --> {i}")

# print("akhir program 1\n")

# # ini dengan range
angka_range = range(5)

for i in angka_range:
    print(f"i sekarang --> {i}")

print("akhir program 2\n")

angka_range = range(1, 5)

for i in angka_range:
    print(f"i sekarang --> {i}")

# print("akhir program 3\n")

# menggunakan string

data_str = "saya ganteng abiess"

for index, huruf in enumerate(data_str):
    print(huruf[0],index)

# print("akhir dari program 4\n")
