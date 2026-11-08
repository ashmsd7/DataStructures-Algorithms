class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        #need to keep track of servers in each row and column, and if any particular row or column has more than or equal to two servers, we just return the number of active servers on that row/column.

        rows = len(grid)
        cols = len(grid[0])

        cnt_row = [0] * rows
        cnt_col = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    cnt_row[i]+=1
                    cnt_col[j]+=1

        res = 0 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (cnt_row[i]>1 or cnt_col[j]>1):
                    res+=1

        return res


        