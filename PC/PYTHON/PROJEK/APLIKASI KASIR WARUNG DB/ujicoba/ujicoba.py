import random

# Fungsi untuk membuat ID random dengan 3 digit angka
def buatIDRandom():
    id_random = ''.join(random.choice('0123456789') for _ in range(3))
    return id_random

# Contoh penggunaan
id_baru = buatIDRandom()
print(f"ID random baru: {id_baru}")
