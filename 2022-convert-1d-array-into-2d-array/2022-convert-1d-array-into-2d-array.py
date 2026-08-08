class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n :
            return []
        
        res = []

        row = []
        idx = 0
        for _ in range(m):        
            for _ in range(n):
                row.append(original[idx])
                idx+=1
            res.append(row)
            row = []
        
        return res