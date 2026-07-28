class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        if N==0:
            return 0
        return N + self.NnumbersSum(N-1)
