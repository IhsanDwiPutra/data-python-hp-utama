# width dan alignment

# data 
nama = "Ihsan"
umur = 20
tinggi = 166.2
sepatu = 45

# string standard
string = f"Nama = {nama}, Umur = {umur}, Tinggi = {tinggi}, No Sepatu = {sepatu}"
print(5*"="+"String Standard"+5*"=")
print(string)

# string multiline
string = f"Nama = {nama}, \nUmur = {umur}, \nTinggi = {tinggi}, \nNo Sepatu = {sepatu}"
print("\n"+5*"="+"String Multiline"+5*"=")
print(string)

# string multiline (kutip triplets
string = f"""
Nama      = {nama}
Umur      = {umur}
Tinggi    = {tinggi}
No Sepatu = {sepatu}"""
print("\n"+5*"="+"String Multiline (kutip triplets)"+5*"=")
print(string)

# mengatur lebar
string = f"""
Nama      = {nama:>5}
Umur      = {umur:>5}
Tinggi    = {tinggi:>5}
No Sepatu = {sepatu:>5}"""
print("\n"+5*"="+"Mengatur Lebar"+5*"=")
print(string)