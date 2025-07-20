nilai8_1 = int(input("niali 8 pertama = "))
nilai7_1 = int(input("nilai 7 pertama = "))
nilai8_2 = int(input("niali 8 kedua = "))
nilai7_2 = int(input("niali 7 kedua = "))

total_benar = nilai8_1 + nilai7_1 + nilai8_2 + nilai7_2
nilai8_1 = nilai8_1 / 8 * 100
nilai8_2 = nilai8_2 / 8 * 100
nilai7_1 = nilai7_1 / 7 * 100
nilai7_2 = nilai7_2 / 7 * 100
total_skor = total_benar / 30 * 100


print("\nNilai 8 pertama = ", int(nilai8_1))
print("Nilai 7 pertama = ", int(nilai7_1))
print("Nilai 8 kedua = ", int(nilai8_2))
print("Nilai 7 kedua = ", int(nilai7_2))
print("skor total = ", int(total_skor))