#data_list = ["aku","ingin","jadi","programmer"]
#gabung = " ".join(data_list)
#print(gabung)

import datetime as dt

lahir = dt.date(2007,4,13)
print(lahir)
today = dt.date.today()
print(f"{today:%A}")
jumlah_hari = today - lahir
print(jumlah_hari.days)

