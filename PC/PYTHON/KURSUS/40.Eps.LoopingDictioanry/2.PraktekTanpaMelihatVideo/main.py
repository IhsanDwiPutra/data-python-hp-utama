# Looping Dictionary

data_dict = {
    "cup": "ucup",
    "oot": "otong",
    "ddg": "dudung"
}

# Looping pertama yang keluar adalah keynya

for dict in data_dict:
    print(dict)

# Menggunakan operator untuk mengambil item / iterables

# Keys
keys = data_dict.keys()
print(keys)

for key in data_dict.keys():
    print(key)

# Values
value = data_dict.values()
print(value)

for value in data_dict.values():
    print(value)

# items
item = data_dict.items()
print(item)

for item in data_dict.items():
    print(item)

for key, value in data_dict.items():
    print(f"Key = {key}\t Value = {value}")
