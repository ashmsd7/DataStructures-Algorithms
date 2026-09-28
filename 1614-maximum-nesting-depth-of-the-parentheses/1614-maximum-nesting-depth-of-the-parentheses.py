class Solution:
    def maxDepth(self, s: str) -> int:
        stacker = []
        ans = 0

        for c in s:
            if c == '(':
                stacker.append(c)
            elif c == ')':
                stacker.pop()
            
            ans = max(len(stacker),ans)
    
        return ans


        