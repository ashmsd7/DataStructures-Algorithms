class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            #Two's complement with fix bit representation giving Memory limit exceeded :(

            num = 2**32 + num

        if num == 0:
            return "0"
        
        test = '0123456789abcdef'

        string = []
        while num:
            rem = num % 16
            string.append(test[rem])
            num = num//16
        
        k = ''.join(string)
        return k[::-1]




