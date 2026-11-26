class Solution:
    def canAliceWin(self, n: int) -> bool:
        #10+9+8+7+6+5+4 => 49,
        remove = 10
        alice = True
        while n>=remove:
            n-=remove
            alice = not alice
            remove-=1
        
        return not alice
            


        

        
        
        