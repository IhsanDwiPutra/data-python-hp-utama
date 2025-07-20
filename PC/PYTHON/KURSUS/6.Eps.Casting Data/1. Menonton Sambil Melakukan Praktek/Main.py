print("==========CASTING DATA==========\n")

print("==========INTEGER==========")
data_int = 5
print("data =", data_int, "type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

print("\n==========FLOAT==========")
data_float = 0.0
print("data =", data_float, "type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

print("\n==========STRING==========")
data_str = "5"
print("data =", data_str, "type =", type(data_str))

data_float = float(data_str)
data_int = int(data_str)
data_bool = bool(data_str)
print("data =", data_float, "type =", type(data_float))
print("data =", data_int, "type =", type(data_int))
print("data =", data_bool, "type =", type(data_bool))

print("\n==========BOOLEAN==========")
data_bool = True
print("data =", data_bool, "type =", type(data_bool))

data_float = float(data_bool)
data_str = str(data_bool)
data_int = int(data_bool)
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_int, "type =", type(data_int))

episode = 6
nama_depan = "Ihsan"
nama_belakang = "Dwi Putra"
panggilan = "Isan"
hari = "Selasa"
tanggal = 17
bulan = "Oktober"
tahun = 2023
print(f"\n\nDibuat oleh {nama_depan} {nama_belakang} ({panggilan})\npada hari {hari}, {tanggal} {bulan} {tahun}\nMengikuti tutorial YT Kelas Terbuka")
print(f"Pada series Python di episode {episode}.")