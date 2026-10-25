class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        # so a closed island is something that satisfies two things
         
        # 1) its a connected body of land that is completely surrounded by water, 000 is a closed island as all 0s are connected , and its a closed island if all 0s are not on boundaries of the grid and all 0s are covered with water.

        #so we will put dfs at every visible 0 that is yet to be added in the unvisited set and work our way accordingly

        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            
            if grid[r][c] == 1 or (r,c) in visited:
                return True
            
            visited.add((r,c))

            #All four directions traversal
            down = dfs(r+1,c)
            right = dfs(r,c+1)
            left = dfs(r,c-1)
            up = dfs(r-1,c)

            return up and down and left and right

        closed_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in visited:
                    if dfs(r,c):
                        closed_islands+=1
        
        return closed_islands
                




        