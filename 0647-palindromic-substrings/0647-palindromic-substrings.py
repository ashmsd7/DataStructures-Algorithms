class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(s):
            return s == s[::-1]
        
        count = 0

        for i in range(len(s)):
            for j in range(i,len(s)):
                curr_str = s[i:j+1]
                if palindrome(curr_str) == True:
                    count+=1

        return count        