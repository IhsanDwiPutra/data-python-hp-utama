# Operator Dictionary

data_dict = {
    "cup": "ucup",
    "tong": "otong",
    "dung": "dudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang Dictioanry = {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"Apakah ada {KEY} ada di data_dict = {CHECKKEY}")

# mengecek value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
# cek key dengan message tidak ditemukan
print(data_dict.get("kis", "key tidak ditemukan"))

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"ihsan": "Ihsan nihhhhh"})  # kalau gak ada diadd aja boss
print(data_dict)

# mendelete data pada dictionary
del data_dict["ihsan"]
print(data_dict)
