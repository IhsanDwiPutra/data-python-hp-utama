print(10*"=" + "Operasi Manipulasi String"+10*"=")

# 1. Menyambung String (Concatenate)
nama_awal = "Ucup"
nama_tengah = "D'"
nama_akhir = "Fame"
nama_lengkap = nama_awal + " " + nama_tengah + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string (lenght)
panjang = len(nama_lengkap)
print("Panjang string "+nama_lengkap+" = " + str(panjang))

# 3. Operator untuk string
# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap +" = " + str(status))

d = "D"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap +" = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap +" = " + str(status))

# mengulang string
print("wk"*15)
print("awok"*10)

# indexing
print("index ke 0 : "+nama_lengkap[0])
print("index ke 6 : " + nama_lengkap[6])
print("index ke (-1) : " + nama_lengkap[-1])
print("index ke (-2) : " + nama_lengkap[-2])
print("index ke (0:4) : " + nama_lengkap[0:3])
print("index ke (3:7) : " + nama_lengkap[3:8])
print("index ke (0,2,4,6,8,10) : " + nama_lengkap[0:11:2])

# item paling kecil
print("item paling kecil : "+ min(nama_lengkap))

# item paling besar
print("item paling besar : "+ max(nama_lengkap))

# ascii code
asciiKode = ord(" ")
print("ASSCI CODE untuk spasi adalah : "+ str(asciiKode))

data = 141
print("char untuk ASCII "+ str(data)+" adalah : "+ chr(data))

# 4. Menghitung dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada "+data+" = " +str(jumlah))