class Solution:
    def hours(self,nums,mid):
        hr=0
        for x in nums:
            hr+=(x+mid-1)//mid
        return hr
        
    def minimumRateToEatBananas(self, nums, h):
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            res = self.hours(nums,mid)
            if res<=h:
                high = mid-1
            else:
                low = mid+1
        return low
