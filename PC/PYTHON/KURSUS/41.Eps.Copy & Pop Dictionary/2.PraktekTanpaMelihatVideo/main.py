# Copy Dictionary

data_dict = {
    "cup": "ucupp",
    "sep": "asep",
    "dug": "dudung",
    "cuy": "ucuy",
    "cok": "coki"
}

data_copy = data_dict.copy()

print(f"Data dict = {data_dict}\n")
print(f"Data Copy = {data_copy}\n")

data_dict["cup"] = "ucup si ganteng"
print(f"Data dict = {data_dict}\n")
print(f"Data Copy = {data_copy}\n")

# Pop dictionary --> berdasarkan key nya
dataAsep = data_copy.pop("sep")
dataCoki = data_copy.pop("cok")
print(f"Data asep = {dataAsep}\n")
print(f"Data Coki = {dataCoki}\n")
print(f"Data Copy = {data_copy}\n")

# Popitem dictionary --> berdasarakan item (key dan valuenya)
dataTerakhir = data_copy.popitem()
print(f"Data terakhir = {dataTerakhir}\n")
print(f"Data copy = {data_copy}\n")
