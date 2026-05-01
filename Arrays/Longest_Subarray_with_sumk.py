class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        max_len =0
        sm=0
        prefix_sum = {}
        for i in range(n):
            sm+=nums[i]
            if sm==k:
                max_len = max(max_len, i+1)
            rem = sm-k
            if rem in prefix_sum:
                ln= i - prefix_sum[rem]
                max_len = max(max_len, ln)

            if sm not in prefix_sum:
                prefix_sum[sm]=i 
        return max_len
