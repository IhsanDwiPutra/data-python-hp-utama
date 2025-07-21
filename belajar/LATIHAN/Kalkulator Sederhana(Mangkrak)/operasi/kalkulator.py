def tambah(*kwargs):
   hasil = 0
   for i in kwargs:
      hasil += i 
   return hasil
   
print(tambah(4,3,4,23,4,2,))