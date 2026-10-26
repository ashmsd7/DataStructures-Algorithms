class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        # so we need to explore islands, and check if the island has a count that is divisible by k... so in dfs function we will make it return True if it satisfied

        #use a global visited set to keep track of islands that have already been visited.

        #as an optimization, we can directly eliminate visited set, and instead change already visited cells to '0' in the grid which prevent our dfs from revisiting.

        rows = len(grid)
        cols = len(grid[0])

        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            
            if grid[r][c] == 0 :
                return 0
            
            val = grid[r][c]
            grid[r][c] = 0

            up = dfs(r-1,c)
            down = dfs(r+1,c)
            left = dfs(r,c-1)
            right = dfs(r,c+1)
        
            return val + up + down + left + right

        cnt = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!=0 :
                    res = dfs(r,c)
                    if res%k==0:
                        cnt+=1
        
        return cnt
                


            

            


        