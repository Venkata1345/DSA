    def findMissingRepeatingNumbers(self, nums):
        ans = []
        sm =0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])
        for i in range(len(nums)):
            sm+=nums[i]
        s = ((n*(n+1))//2) - sm + ans[0]
        ans.append(s)
        return ans
