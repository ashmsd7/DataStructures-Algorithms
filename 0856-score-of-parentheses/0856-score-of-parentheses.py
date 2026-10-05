class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 1

        for i in range(1,len(s)):
            if s[i] == '(':
                depth+=1
            else:
                if s[i-1] == '(':
                    score+= 2**(depth-1)
                
                depth-=1
            
        
        return score
        
                
                   


            


        