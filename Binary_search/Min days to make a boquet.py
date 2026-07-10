class Solution:
    def check(self,nums,k,m,d):
        c=0
        adj=0
        for i in range(len(nums)):
            if nums[i]<=d:
                c+=1
            else:
                adj+=(c//k)
                c=0
        adj+=(c//k)
        return adj>=m

    def roseGarden(self, n, nums, k, m):
        val=m*k
        if val>n:
            return -1
        low = min(nums)
        high = max(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.check(nums,k,m,mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans


     
