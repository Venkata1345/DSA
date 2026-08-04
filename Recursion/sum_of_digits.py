class Solution:
    def addDigits(self, num):
        #your code goes here
        if num<10:
            return num
        return self.addDigits(self.check(num))
    def check(self,num):
        if (num==0):
            return 0
        return (num%10)+self.check(num//10)
 
