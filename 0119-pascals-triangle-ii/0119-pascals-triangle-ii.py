class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        curr_row = [1,1]
        
        for i in range(2,rowIndex+1):
            for j in range(len(curr_row)-1,0,-1):
                curr_row[j]+= curr_row[j-1]
            curr_row.append(1)
        
        return curr_row
        
        