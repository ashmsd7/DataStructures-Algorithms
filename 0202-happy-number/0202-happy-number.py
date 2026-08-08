class Solution:
    def isHappy(self, n: int) -> bool:
        Seen = set()
        return self.square_digits(Seen,n)
    def square_digits(self,Seen,n):
        res = 0
        for digit in str(n):
            res+= int(digit) * int(digit)
        
        if res == 1:
            return True
        if res in Seen:
            return False
        Seen.add(res)
        return self.square_digits(Seen,res)
        