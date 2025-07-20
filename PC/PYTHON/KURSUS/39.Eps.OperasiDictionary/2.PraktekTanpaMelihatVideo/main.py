# Operasi Dictionary

data_dict = {
    "cup": "Ucup",
    "tog": "Otong",
    "ddg": "Dudung"
}

# Menghitung panjang dictionary
LEN = len(data_dict)
print(f"Panjang Dictionary = {LEN}")

# Mengecek key yang sedang exist atau tidak
KEY = "tog"
CHECKKEY = KEY in data_dict
print(f"Apa {KEY} ada di dictionary = {CHECKKEY}")

# Mengambil data read menggunakan get
print(data_dict["ddg"])
print(data_dict.get("cup"))
# mengambil dengan menggunakan pesan tidak ada
print(data_dict.get("kis", "Tidak ditemukan"))

# Mengupdate dictionary
data_dict["cup"] = "ucup ganteng bengettt"
# menggunakan update
data_dict.update({"ihsan": "ihsan nihh boy"})
print(data_dict)

# Mendelete dictionary

del data_dict["cup"]
del data_dict["ihsan"]
print(data_dict)
