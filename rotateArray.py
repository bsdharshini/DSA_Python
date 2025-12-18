# 1 Reverse the entire array
# 2 Reverse the first k elements
# 3 Reverse the remaining n-k elements
def reverseArray(left,right,arr):
    while(left<right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left +=1
        right -=1
def rotateArray(arr):
    left = 0 
    right = len(arr)-1
    k = 3
    while(left < k):# 1st reverse
        temp = arr[left]
        arr[left]= arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    reverseArray(0,k-1,arr) # 2nd reverse
    reverseArray(k,len(arr)-1,arr) #3rd reverse
arr = [1,2,3,4,5,6]
rotateArray(arr)
print(arr)
        
