class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        Factors = set()
        d = 2
        while d * d <=n:
            while n%d == 0:
                Factors.add(d)
                n = n//d

            d+=1

        if n>1:
            Factors.add(n)

                
        for val in Factors:
            if val not in {2,3,5}:
                return False
        return True
        

        