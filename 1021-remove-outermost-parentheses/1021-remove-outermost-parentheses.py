class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        balance = 0 
        for i in range(len(s)):
            if s[i] == '(':
                if balance != 0 :
                    res+=s[i]
                balance+=1
            
            else:
                if balance !=1:
                    res+=s[i]
                balance-=1
        
        return res
        