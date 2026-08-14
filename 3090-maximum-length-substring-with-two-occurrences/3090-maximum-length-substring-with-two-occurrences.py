class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hash = {}
        idx = 0
        max_len = 0
        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i],0) + 1
            while hash[s[i]] > 2:
                hash[s[idx]]-=1
                idx+=1
            
            max_len = max(max_len , i-idx+1)
    
        return max_len



        