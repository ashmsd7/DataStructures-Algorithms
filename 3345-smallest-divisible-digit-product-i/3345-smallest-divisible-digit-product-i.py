class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current = n
        while True:
            product = 1
            for digit in str(current):
                if int(digit) == 0:
                    return current
                product*=int(digit)
            
            if product%t == 0:
                return current
            current+=1
            


        