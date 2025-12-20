class PrefixSum:
    def __init__(self,nums):
        self.prefix_sum = 0
        self.nums = nums
        self.freq = {0:1}
        self.count = 0
        
    def sumArr(self,k,n):
        #if k found in either by combining consecutive nums then increase count else add to freq dict
        for num in self.nums:
            self.prefix_sum += num
            if self.prefix_sum - k in self.freq:
                self.count += self.freq[self.prefix_sum - k]
            self.freq[self.prefix_sum] = self.freq.get(self.prefix_sum,0)+1
        return self.count
        
nums = [1,2,3,4,3]
n = len(nums)
numArray = PrefixSum(nums)
k = 3
print(numArray.sumArr(k,n))


    
