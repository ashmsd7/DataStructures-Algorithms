class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        colSum = [0]*n
        rowSum = [0]*m

        for i in range(m):
            currRow = 0
            for j in range(n):
                currRow+=mat[i][j]
            
            rowSum[i] = currRow

        for j in range(n):
            currCol = 0
            for i in range(m):
                currCol+=mat[i][j]
            
            colSum[j] = currCol
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if rowSum[i] == 1 and colSum[j]==1 and mat[i][j] == 1:
                    ans+=1
        
        return ans