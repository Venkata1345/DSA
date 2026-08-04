class Solution:
    def isSorted(self, nums):
        #your code goes here
        return self.check(nums,0)
    
    def check(self,nums,i):
        if i>=len(nums)-1:
            return True
        if nums[i]>nums[i+1]:
            return False
        return self.check(nums,i+1)
