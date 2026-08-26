class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        n = len(s)
        curr_len = n + 1
        res = ""
        count = 0

        for r in range(n):
            if s[r] == '1':
                count+=1
            
            if count == k :

                while s[l] == '0':
                    l+=1
                cur_str = s[l:r+1]

                if r - l + 1 < curr_len:
                    curr_len = r - l + 1
                    res = cur_str
                elif r - l + 1 == curr_len and cur_str < res:
                    res = cur_str

                count-=1
                l+=1
        
        return res

        