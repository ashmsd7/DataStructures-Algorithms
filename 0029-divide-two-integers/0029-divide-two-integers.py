class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        if divisor < 0:
            neg = not neg
        if dividend < 0:
            neg = not neg
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            mul = 1
            temp = divisor
            while temp + temp < dividend:
                temp+=temp
                mul+=mul
            dividend-=temp
            quotient+=mul
        if neg :
            quotient = -(quotient)
        
        if quotient < -2147483648:
            return -2147483648
        if quotient > 2147483647:
            return 2147483647
        return quotient





        