class Solution:
    def minimumPushes(self, word: str) -> int:
        push= 0
        for i in range(len(word)):
            push = 1 + push + (i)// 8 
        return push
        

        
        


        