class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        n = len(s)
        prev = s[0]
        for i in range(1,n):
            if i%2==0:
                prev = s[i]
                continue
            if s[i]!=prev:
                changes+=1
        
        return changes
            



        