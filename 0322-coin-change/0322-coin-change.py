class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def minimum_coins(amt):

            if amt in memo:
                return memo[amt]
            
            minimum = float('inf')

            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                
                minimum = min(minimum, 1 + minimum_coins(diff))
            
            memo[amt] = minimum
            return memo[amt]
        
        result = minimum_coins(amount)
        if result < float('inf'):
            return result
        return -1


        