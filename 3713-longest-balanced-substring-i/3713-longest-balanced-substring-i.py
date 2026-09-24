class Solution:
    def longestBalanced(self, s: str) -> int:
        
        max_len = 0

        for left in range(len(s)):
            List = [0] * 26
            for right in range(left,len(s)):
                List[ord(s[right])-ord('a')]+=1
                max_val = max(List)
                balanced = True
                for val in List:
                    if val > 0 and val!=max_val:
                        balanced = False
                        break
                if balanced:
                    max_len = max(max_len,right-left+1)

        return max_len
                

        