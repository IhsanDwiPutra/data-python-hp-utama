from copy import deepcopy
data_0 = [1, 2]
data_1 = [3, 4]

data_2d = [data_0, data_1, 10]
data_2d_copy = data_2d.copy()

print(f"data = {data_2d}")
print(f"data_copy = {data_2d_copy}")

# mengambil data dari nested list

data = data_2d[1][1]
print(f"data = {data}")

# address semuanya

print(f"address data_2d = {hex(id(data_2d))}")
print(f"address data_2d copy = {hex(id(data_2d_copy))}")

print("addreess dari member ke-1")
print(f"address data_2d = {hex(id(data_2d[0]))}")
print(f"address data_2d copy = {hex(id(data_2d_copy[0]))}")

data_2d[1][0] = 5
data_2d[2] = 9
print(f"data = {data_2d}")
print(f"data_copy = {data_2d_copy}")

# kita gunakan deepcopy

data_2d = [data_0, data_1, 10]
data_2d_deepcopy = deepcopy(data_2d)

print(f"address data_2d = {hex(id(data_2d))}")
print(f"address data 2d deepcopy = {hex(id(data_2d_deepcopy))}")

print("addreess dari member ke-1")
print(f"address data_2d = {hex(id(data_2d[0]))}")
print(f"address data 2d deepcopy = {hex(id(data_2d_deepcopy[0]))}")

data_2d[1][0] = 30
print(f"data = {data_2d}")
print(f"data_copy = {data_2d_copy}")
print(f"data 2d deepcopy = {data_2d_deepcopy}")
