class Solution:
    def reverseParentheses(self, s: str) -> str:
        depth = 0
        hasher = {0 :""}
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                depth+=1
                hasher[depth] = ""
            
            elif s[i] == ')':
                curr = hasher[depth][::-1]

                depth-=1
                hasher[depth]+= curr
            
            else:
                hasher[depth]+=s[i]
        
            i+=1
        
        return hasher[0]