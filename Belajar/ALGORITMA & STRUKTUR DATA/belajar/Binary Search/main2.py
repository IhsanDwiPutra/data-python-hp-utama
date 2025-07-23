def binary_search(data, target):
   low = 0 
   high = len(data) - 1 
   while low <= high:
      mid = (low + high) // 2
      if data[mid] == target:
         return mid
      elif data[mid] < target:
         low = mid + 1
      else:
         high = mid - 1
   return "Target tidak ditemukan"


list = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(list,6))