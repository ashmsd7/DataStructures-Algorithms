class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - minimum
            max_profit = max(profit,max_profit)

            minimum = min(prices[i],minimum)
        
        return max_profit
            
        

        