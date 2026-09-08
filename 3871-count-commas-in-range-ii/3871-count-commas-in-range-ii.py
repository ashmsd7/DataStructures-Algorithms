class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        lower = 1000
        commas = 0
        cur_commas = 1

        while n >= lower:
            upper = lower * (10**3) - 1
            if n < upper :
                commas += cur_commas *(n - lower + 1)
                return commas
            commas += (upper - lower + 1) * cur_commas
            cur_commas +=1
            lower = upper + 1
            upper = lower * (10**3) - 1
        
        return commas 
                
            

        