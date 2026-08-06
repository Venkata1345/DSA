class Solution:    
    def myPow(self, x, n):
        #your code goes here
        if n==0:
            return 1
        if n<0:
            return 1/(self.myPow(x,-n))
        half = self.myPow(x,n//2)
        if n%2==0:
            return half*half
        return x*half*half
