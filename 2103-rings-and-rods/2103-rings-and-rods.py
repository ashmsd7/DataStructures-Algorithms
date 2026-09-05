class Solution:
    def countPoints(self, rings: str) -> int:
        hasher = {i: set() for i in range(10)}

        for i in range(0,len(rings),2): 
            color = rings[i]
            rod = int(rings[i+1])
            hasher[rod].add(color)
        
        count = 0
        for rod in hasher:
                if len(hasher[rod]) == 3:
                    count+=1

        return count        
        