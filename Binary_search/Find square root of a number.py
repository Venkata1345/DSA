class Solution:
    def floorSqrt(self, n: int) -> int:
        if n==0:
            return 0
        low = 0
        high = n
        while low<=high:
            mid = (low+high)//2
            if mid*mid <= n:
                low = mid+1
            else:
                high = mid-1
        return high
