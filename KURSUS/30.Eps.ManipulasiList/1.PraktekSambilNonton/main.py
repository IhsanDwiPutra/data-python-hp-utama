# Manipulasi data List

# Operasi

# index  0(-3)      1(-2)      2(-1)
data = ["ucup", "otong", "Dudung"]

# mengambil data dari list tersebut
data_0 = data[0]
print(f"data pertama (index 0) = {data_0} ")

data_terakhir = data[-1]
print(f"data terakhir adalah (index -1) = {data_terakhir} ")

data_ucup = data[-3]
print(f"data ucup = {data_ucup} ")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

#  manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah \n{data}")
data.insert(1, "Asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Ucok")
print(f"data ditambah lagi = \n {data}")

# menambahkan list dengan list
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data kedua menjadi michael
data[2] = "Michael"
print(f"data rubah = {data}")

# meremove data
data.remove("Ujang")
print(f"data remove = {data}")
# data.remove akan error karena harus sesuai

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = {data}")

print(data_akhir)
