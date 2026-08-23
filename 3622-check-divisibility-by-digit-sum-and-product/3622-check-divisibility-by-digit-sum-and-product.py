class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        digit_sum = 0
        digit_product = 1

        while x>0:
            digit = x%10
            digit_sum+=digit
            digit_product*=digit
            x=x//10
        
        res = digit_sum + digit_product

        if (n%res == 0):
            return True
        return False
        