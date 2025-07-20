## ----LIST----##

# Kumpulan data numbers
data_angka = [1, 7, 3, 6, 3]
print(data_angka)

# kumpulan data string
data_string = ["ucup", "otong", "odah"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan campuran
data_campuran = [1, "bala-bala", 2, "cireng", "ucup", True, "otong", False]
print(data_campuran)

# cara alternataif membuat list
data_range = range(0, 10, 2)  # range (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop
list_pake_for = [i**2 for i in range(0, 11)]
print(list_pake_for)

# membuat list pake for pake if
lis_for_if = [i for i in range(0, 10)if i != 5]
print(lis_for_if)

lis_for_if = [i for i in range(0, 10)if i % 2 == 0]
print(lis_for_if)

lis_for_if = [i for i in range(0, 10)if i % 2 != 0]
print(lis_for_if)
