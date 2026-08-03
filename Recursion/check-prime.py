class Solution:
    def checkPrime(self, num):
        #your code goes here
        if num<=1:
            return False
        return self.check(num,2)
    
    def check(self,num,i):
        if i> num**0.5:
            return True
        if num%i==0:
            return False
        return self.check(num,i+1)
