    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            need_num = target - num 
            if need_num in seen:
                return [seen[need_num], i]
            seen[num] = i 
