#Precalculate the arr sum before only. So in the sumArr call it will be just O(1) not O(n). 
#Prefix sum
class RangeSum:
    def __init__(self,nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1]+num) # append the current number + last prefix element(-1) 
    def sumArr(self,left,right):
        return self.prefix[right+1]-self.prefix[left] # right - left value 
        
nums = [-3,1,2,-2,4,5]
numArray = RangeSum(nums)
print(numArray.sumArr(0,2))
print(numArray.sumArr(1,4))
print(numArray.sumArr(0,4))

    
