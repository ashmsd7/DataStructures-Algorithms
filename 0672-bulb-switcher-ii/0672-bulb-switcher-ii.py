class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        #Hmm. So, math equation again. I am thinking maybe sum like -> Graph & check all possibilities. BUt how to find the equation bra.?

        # Button 2 + Button 2 -> Nothing. Lol. 

        # Answer cannot exceed 8 as only 8 possible distinct states can be attained.
        if presses == 0:
            return 1
        
        if n == 1:
            return 2
        
        if n==2 and presses == 1:
            return 3
        
        if n==2 or presses == 1:
            return 4
        
        if presses == 2:
            return 7
        
        if presses > 2:
            return 8
        
        




        