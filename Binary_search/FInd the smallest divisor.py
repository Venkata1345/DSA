class Solution:
    def sm(self,nums,mid):
        sm=0
        for i in range(len(nums)):
            sm+= (nums[i]+mid-1)//mid
        return sm
    def smallestDivisor(self, nums, limit):
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            sumd = self.sm(nums,mid)
            if sumd<=limit:
                high = mid-1
            else:
                low = mid+1
        return low
