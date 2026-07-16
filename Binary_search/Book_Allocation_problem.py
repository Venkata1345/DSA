class Solution:
    def check(self,nums,pages):
        students=1
        running =0
        for i in range(len(nums)):
            if running + nums[i] <= pages:
                running+=nums[i]
            else:
                students+=1
                running=nums[i]
        return students

        

    def findPages(self, nums, m):
        if m>len(nums):
            return -1
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = (low+high)//2
            if self.check(nums,mid)>m:
                low=mid+1
            else:
                high = mid-1
        return low     
       
