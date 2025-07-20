import tkinter as tk

def hello():
    label.config(text="Hello, World!")

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh GUI dengan Tkinter")

# Membuat label dan tombol
label = tk.Label(root, text="Tekan tombol di bawah")
label.pack()

button = tk.Button(root, text="Klik Saya", command=hello)
button.pack()

# Menjalankan aplikasi
root.mainloop()
