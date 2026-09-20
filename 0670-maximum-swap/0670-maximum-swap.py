class Solution:
    def maximumSwap(self, num: int) -> int:
        str_int = list(str(num))

        hasher ={}

        for i , digit in enumerate(str_int):
            hasher[digit] = i

        for i in range(len(str_int)):
            for d in range(9,int(str_int[i]),-1):
                if str(d) in hasher and hasher[str(d)] > i:
                    last_idx = hasher[str(d)]     

                    str_int[i] , str_int[last_idx] = str_int[last_idx] , str_int[i]

                    return int("".join(str_int))
                
        
        return num