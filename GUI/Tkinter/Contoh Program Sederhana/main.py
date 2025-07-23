import tkinter as tk

# membuat jendela utama
window = tk.Tk()
window.title("Halo Tkinter")
window.geometry("300x200") # ukuran lebar x tinggi

# menambahkan label
label = tk.Label(window, text="Halo, dunia yang Fanaaaa", font=("Arial", 14))
label.pack(pady=20)

# menambahkan tombol
def saat_diklik():
	label.config(text="Tombol diklik!")

tombol = tk.Button(window, text="Klik saya bang", command=saat_diklik)
tombol.pack()

# menjalankan aplikasi
window.mainloop()