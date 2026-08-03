class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        return self.check(s,0,len(s)-1)
    
    def check(self,s,l,r):
        if l>=r:
            return True
        if s[l]!=s[r]:
            return False
        return self.check(s,l+1,r-1)
