class Solution:
    def NthRoot(self, n, m):
        low = 1
        high = m
        while low <=high:
            mid = (low+high)//2
            midN = mid**n 
            if midN == m:
                return mid 
            elif midN > m:
                high = mid-1
            else:
                low = mid +1
        return -1
