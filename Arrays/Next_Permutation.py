    def nextPermutation(self, nums):
        # Your code goes here
        n= len(nums)
        pivot = 0
        for i in range(n-1,0,-1):
            if nums[i-1]<nums[i]:
                pivot = i
                break
        if pivot ==0:
            nums.reverse()
            return 
        
        for i in range(n-1,pivot-1,-1):
            if nums[i]>nums[pivot-1]:
                nums[i],nums[pivot-1]= nums[pivot-1], nums[i]
                break
        
        nums[pivot:] = reversed(nums[pivot:])
        return
