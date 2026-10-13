class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        # reminds me of Maxpooling in CNNs using a kernel/filter.
        rows , cols = len(grid) , len(grid[0])
        
        res = [[0]* (cols - 2) for _ in range(rows-2)]

        for i in range(rows-2):
            for j in range(cols-2):

                curr_max = 0

                for k in range(i,i+3):
                    for l in range(j,j+3):
                        curr_max = max(curr_max,grid[k][l])
                
                res[i][j] = curr_max

        return res                




        