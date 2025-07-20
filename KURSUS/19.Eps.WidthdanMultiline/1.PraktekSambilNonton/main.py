print(5*"="+"Width dan Multiline"+5*"=")

# data
nama = "Ucup"
umur = 18
tinggi = 165.5
noSepatu = 43

# string standard
string = f"Nama = {nama}, Umur = {umur}, Tinggi = {tinggi}, No Sepatu = {noSepatu}"
print("\n"+5*"="+"Data String Standard"+5*"=")
print(string)

# string multiline
string = f"Nama = {nama}, \nUmur = {umur}, \nTinggi = {tinggi}, \nNo Sepatu = {noSepatu}"
print("\n"+5*"="+"Data String Multiline"+5*"=")
print(string)

# string Multiline (kutip triplets)
string = f"""Nama = {nama},
Umur = {umur}, 
Tinggi = {tinggi}, 
No Sepatu = {noSepatu}"""
print("\n"+5*"="+"Data String Multiline (kutip triplets)"+5*"=")
print(string)

# Mengatur lebar
string = f"""
Nama      = {nama:<5}
Umur      = {umur:^5}
Tinggi    = {tinggi:>5}
No Sepatu = {noSepatu:>5}"""
print("\n"+5*"="+"Mengatur lebar"+5*"=")
print(string)
