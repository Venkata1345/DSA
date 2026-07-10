class Solution:
    def canplacecows(self,nums,dist,cows):
        cow_count=1
        last=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-last>=dist:
                cow_count+=1
                last=nums[i]
            if cow_count>=cows:
                return True
        return False
    def aggressiveCows(self, nums, k):
        nums.sort()
        low = 1
        high = max(nums)-min(nums)
        while low<=high:
            mid = (low+high)//2
            if self.canplacecows(nums,mid,k):
                low=mid+1
            else:
                high = mid-1
        return high
        
