class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        #dp[i][j] will deal with values that are coming from both left AND top right, so when we do assignment, first we do dp = left then we do dp = top, so values override, instead we can do something like union like dp = left | top
        
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                
                x = grid[i][j]

                from_top = {val ^ x for val in dp[i-1][j]} if i>0 else set()
                from_left = {val ^ x for val in dp[i][j-1]} if j>0 else set()

                dp[i][j] = from_top | from_left
                
        return min(dp[-1][-1])
                


        


        
        