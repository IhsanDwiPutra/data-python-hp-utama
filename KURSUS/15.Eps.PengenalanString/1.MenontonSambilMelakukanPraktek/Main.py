print(15*"=" + "PENGENALAN STRING" + 15*"=")


data = "ini adalah string"
print(data)
print(type(data))

# 1 cara membuat string

'''
   1. dengan menggunakan single quote
   2. dengan menggunakan double quote
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("ini adalah hari jum'at")

# 2. menggunakan tanda \
# membuat tanda  ini menjasmdi string
print('mari shalat jum\'at')
print('g\'day isn\'t it?')

# backslash
print("C:\\USER\\BOLU")

# tab
print("ucup \t\t\totong semakin jauhan")


# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama\nbaris kedua") # LF -- LINE FEED  > unix,macos
print("baris pertama. \rbaris kedua") # CR -- CARRIAGE RETURN
print("baris pertama.\r\nbaris kedua") # CRLF -- LINE FEED CARRIAGE RETURN > windows

# 3. string literal atau raw string

print(r'C:\n\b')

# multiline literal string
print("""
NAMA : IHSAN
KELAS: 12
""")

#multiline literal string dan raw
print(r"""
WEB:www.com\b\n""")
    
