class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        rows , cols = len(heights) , len(heights[0])
        pacific , atlantic = set(),set()

        def dfs(row, col, visited, prevHeight):
            if (row<0 or col<0 or row == len(heights) or col == len(heights[0])) or (heights[row][col]< prevHeight) or ((row,col) in visited):
                return
            
            visited.add((row,col))
            dfs(row+1,col,visited,heights[row][col])
            dfs(row-1,col,visited,heights[row][col])
            dfs(row,col+1,visited,heights[row][col])
            dfs(row,col-1,visited,heights[row][col])

        for c in range(cols):
            #All columns in first row.(All elements)
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1 , c , atlantic, heights[rows-1][c])
        
        for r in range(rows):
            #All rows in first and last column.
            dfs(r,cols-1,atlantic,heights[r][cols-1])
            dfs(r,0 , pacific, heights[r][0])
        
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        
        return res

        


        