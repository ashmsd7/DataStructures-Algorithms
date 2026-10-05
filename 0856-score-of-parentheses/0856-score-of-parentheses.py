class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for i in range(1,len(s)):
            if s[i] == '(':
                depth+=1
            else:
                if s[i-1] == '(':
                    score+= 2**(depth)
                
                depth-=1
            
        
        return score
        
                
                   


            


        