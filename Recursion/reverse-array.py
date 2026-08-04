class Solution:
    def reverseArray(self, nums):
        #your code goes here
        self.reverse(nums,0,len(nums)-1)
        return nums

    
    def reverse(self,nums,l,r):
        if l>=r:
            return 
        nums[l],nums[r]=nums[r],nums[l]
        self.reverse(nums,l+1,r-1)
