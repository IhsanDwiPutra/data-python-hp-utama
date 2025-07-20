print(10*"=","CASTING DATA",10*"=","\n")

print(10*"=","INTEGER",10*"=")
data_int = 5
print(f"Data = {data_int}\tType = {type(data_int)}")
print("Dicasting",5*"=",">")
data_float = float(data_int)
data_string = str(data_int)
data_boolean = bool(data_int)
print(f"Data = {data_float}\tType = {type(data_float)}")
print(f"Data = {data_string}\tType = {type(data_string)}")
print(f"Data = {data_boolean}\tType = {type(data_boolean)}")

print("\n",20*"=","\n")

print(10*"=","FLOAT",10*"=")
data_float = 5.0
print(f"Data = {data_float}\tType = {type(data_float)}")
print("Dicasting",5*"=",">")
data_integer = int(data_float)
data_string = str(data_float)
data_boolean = bool(data_float)
print(f"Data = {data_integer}\tType = {type(data_integer)}")
print(f"Data = {data_string}\tType = {type(data_string)}")
print(f"Data = {data_boolean}\tType = {type(data_boolean)}")

print("\n",20*"=","\n")

print(10*"=","STRING",10*"=")
data_string = "5"
print(f"Data = {data_string}\tType = {type(data_string)}")
print("Dicasting",5*"=",">")
data_integer = int(data_string)
data_float = float(data_string)
data_boolean = bool(data_string)
print(f"Data = {data_integer}\tType = {type(data_integer)}")
print(f"Data = {data_float}\tType = {type(data_float)}")
print(f"Data = {data_boolean}\tType = {type(data_boolean)}")

print("\n",20*"=","\n")

print(10*"=","BOOLEAN",10*"=")
data_boolean_1 = True
data_boolean_2 = False
print(f"""Data 1 = {data_boolean_1}\tType = {type(data_boolean_1)}
Data 2 = {data_boolean_2}\tType = {type(data_boolean_1)}""")
print("Dicasting",5*"=",">")

data_integer_1 = int(data_boolean_1)
data_integer_2 = int(data_boolean_2)
data_string_1 = str(data_boolean_1)
data_string_2 = str(data_boolean_2)
data_float_1 = float(data_boolean_1)
data_float_2 = float(data_boolean_2)

print(f"""Data 1 = {data_integer_1}\tType = {type(data_integer_1)}
Data 2 = {data_integer_2}\tType = {type(data_integer_1)}""")
print(f"""Data 1 = {data_string_1}\tType = {type(data_string_1)}
Data 2 = {data_string_2}\tType = {type(data_string_1)}""")
print(f"""Data 1 = {data_float_1}\tType = {type(data_float_1)}
Data 2 = {data_float_2}\tType = {type(data_float_1)}""")

episode = 6
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Senin"
tanggal = 25
bulan = 12
if bulan == 1:
    bulan = "Januari"
elif bulan == 2:
    bulan = "Februari"
elif bulan == 3:
    bulan = "Maret"
elif bulan == 4:
    bulan = "April"
elif bulan == 5:
    bulan = "Mei"
elif bulan == 6:
    bulan = "Juni"
elif bulan == 7:
    bulan = "Juli"
elif bulan == 8:
    bulan = "Agustus"
elif bulan == 9:
    bulan = "September"
elif bulan == 10:
    bulan = "Oktober"
elif bulan == 11:
    bulan = "November"
elif bulan == 12:
    bulan = "Desember"
else:
    bulan = "?"

tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")