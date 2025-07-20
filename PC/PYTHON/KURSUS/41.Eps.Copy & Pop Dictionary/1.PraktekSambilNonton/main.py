# Copy Dictionary

data_dict = {
    "cup": "ucup surucup",
    "tong": "otong surotong",
    "dung": "dudung mardudung",
    "sep": "asyep si kasep",
    "cuy": "ucuy si kucuy"
}

frien = data_dict.copy()

print(f"Data dict : {data_dict}\n")
print(f"frien : {frien}\n")

data_dict["cup"] = "ucup baik banget"
print(f"Data dict : {data_dict}\n")
print(f"frien : {frien}\n")

# pop dictionary
dataAsep = frien.pop("sep")
dataUcup = frien.pop("cup")
print(f"Data asep = {dataAsep}\n")
print(f"Data Ucup = {dataUcup}\n")
print(f"Data frien = {frien}\n")

# popitem dictionary
dataTerakhir = frien.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"Data frien = {frien}\n")
