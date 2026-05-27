class Solution:
    def rotateArray(self, nums, k: int) -> None:
        #optimized in-place
        n= len(nums)
        k = k%n
        def rev(arr,l,r):
            while l<=r:
                arr[l],arr[r] = arr[r],arr[l]
                l+=1
                r-=1
            return arr
        l=0
        r = n-1
        rev(nums,l,r)

        l=0
        r=n-k-1
        rev(nums,l,r)


        l=n-k
        r=n-1
        return rev(nums,l,r)
