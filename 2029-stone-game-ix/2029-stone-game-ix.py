class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        hasher = {}
        for stone in stones:
            r = stone  % 3
            hasher[r] = hasher.get(r,0) + 1
        
        num_zeros = hasher.get(0,0) 
        num_zeros = num_zeros%2
        num_ones = hasher.get(1,0)
        num_twos = hasher.get(2,0) 
        
        n = len(stones)

        if (num_ones == 0 or num_twos == 0):
            return (abs(num_ones - num_twos) >=3  and num_zeros%2 == 1)
        
        else:
            if num_zeros % 2 == 1:
                return abs(num_ones - num_twos) > 2
            else:
                return True
        

        









                    

        





        


        