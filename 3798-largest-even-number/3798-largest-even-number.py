class Solution:
    def largestEven(self, s: str) -> str:
        if s == '1':
            return ""
        
        while s and int(s[-1]) == 1:
            s = s[:-1]
        
        return s
        


        