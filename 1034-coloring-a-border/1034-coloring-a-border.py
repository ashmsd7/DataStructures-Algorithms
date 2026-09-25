class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        rows , cols = len(grid),len(grid[0])
        visited , border = set() , set()

        def dfs(roww,coll):
            if roww < 0 or roww >= rows or coll < 0 or coll>=cols:
                return False
            
            visited.add((roww,coll))

            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            color = grid[roww][coll]

            for nr , nc in directions:
                nr = roww + nr
                nc = coll + nc
                if nr < 0 or nr >=rows or nc < 0 or nc>=cols:
                    border.add((roww,coll))
                
                elif grid[nr][nc]!= color:
                    border.add((roww,coll))
                
                elif (nr,nc) not in visited:
                    dfs(nr,nc)
        
        dfs(row,col)

        for (r,c) in border:
            grid[r][c] = color
        
        return grid
                





        