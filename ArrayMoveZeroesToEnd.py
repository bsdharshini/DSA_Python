#Move Zeroes to End
# Time complexity - O(n), Space complexity O(1)
def moveZerosToEnd(arr):
  index = 0
  n = len(arr)
  for i in range(n):
    if arr[i] !=0:
      arr[index] = arr[i]
      index +=1
  while(index<n):
    arr[index]=0
    index +=1

arr = [1,2,0,3,0,4]
moveZerosToEnd(arr)
print(arr)
    
