# Find Max & Min 
# Using 2 pointer variable find the min and max
def minMax(arr):
  minNum = arr[0]
  maxNum = arr[0]
  n = len(arr)
  for i in range(n):
    if arr[i] < minNum:
      minNum = arr[i]
    if arr[i]>maxNum:
      maxNum = arr[i]
  return(minNum,maxNum)

arr = [1,2,3,4,5,6]
valueNum = minMax(arr)
print(valueNum)
