class Solution:
    def factorial(self, n):
        #Your code goes here
        if n<2:
            return 1
        return n*self.factorial(n-1)
