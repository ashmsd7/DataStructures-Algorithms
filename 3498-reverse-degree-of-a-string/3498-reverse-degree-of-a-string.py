class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            char = s[i]
            val = ord('z') - ord(char) + 1
            res+=val*(i+1)
        
        return res
        