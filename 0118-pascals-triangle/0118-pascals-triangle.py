class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1],[1,1]]
        
        res = [[1],[1,1]]
        for i in range(2,numRows):
            prev_row = res[i-1]
            row = [1]
            for j in range(1,len(prev_row)):
                row.append(prev_row[j-1]+prev_row[j])
            res.append(row+[1])
        return res
        
            