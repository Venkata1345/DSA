class Solution:
    def arraySum(self, nums):
        #your code goes here
        return self.sm(nums,0)
    
    def sm(self,nums,i):
        if i>=len(nums):
            return 0
        return nums[i]+self.sm(nums,i+1)
