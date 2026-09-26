class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hasher = {}
        for k in knowledge:
            hasher[k[0]] = k[1]
        
        res = ""
        i = 0

        while i < len(s):
            if s[i]!='(':
                res+=s[i]
                i+=1
                continue
            
            j = i+1
            while s[j]!=')':
                j+=1

            curr_str = s[i+1:j]
            
            if curr_str in hasher:
                res+=hasher[curr_str]
            
            else:
                res+='?'

            i = j+1
        
        return res

            
        