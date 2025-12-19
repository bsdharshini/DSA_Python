#Reversed the array using 2 pointer logic. 
# Time complexity - O(n), Space complexity O(1)
def reverseArray(arr):
  left = 0
  right = len(arr)-1
  while(left<right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left +=1
    right -=1

arr = [1,2,3,4,5,6]
reverseArray(arr)
print(arr)
