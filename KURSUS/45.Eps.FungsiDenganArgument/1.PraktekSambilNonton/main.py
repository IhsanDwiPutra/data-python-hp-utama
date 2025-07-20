'''Fungai dengan argument (input)'''

# Template
#def nama_fungsi(argument):
#    badan_fungsi

def hell(nama):
    print(f"Say hello kepada yang terhormat yaitu \"{nama}\"")
    
hell("Ucup Markucup")

# program tambah
def tambah(angka_1,angka_2):
    #fungsi tambah
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil} ")
    
tambah(4,5)
tambah(10,7)

def say_hi(member):
    
    data_member = member.copy()
    member[1] = "aseyepp"
    for peserta in data_member:
        print(f"Hallo {peserta}")
        
daftar = ["ucok","ujang","mali"]

say_hi(daftar)

print(daftar[1])

def penjumlahan(angka):
    data_penjumlah = angka.copy()
    for index,data in enumerate(data_penjumlah):
        print(f"{index+1}. ini {data}")
        
orang = ["yanto","yanti","marni"]

penjumlahan(orang)