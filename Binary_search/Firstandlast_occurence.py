class Solution:

    def firstOccurence(self, nums, target):
        low,high = 0,len(nums)-1
        first = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                first = mid
                high = mid+1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return first
    
    def LastOccurence(self,nums,target):
        low,high = 0,len(nums)-1
        last = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                last = mid
                low = mid+1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return last
    def searchRange(self, nums, target):
        first = self.firstOccurence(nums,target)
        if first == -1:
            return [-1,-1]
        
        last = self.LastOccurence(nums,target)
        return [first,last]
                
