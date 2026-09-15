class Solution:
    def countSubstrings(self, s: str) -> int:
        total_pal = 0
        for i in range(len(s)):
            even = self.CheckPalindrome(s,i,i+1)
            odd = self.CheckPalindrome(s,i,i)
            total_pal+= even + odd
        
        return total_pal
    
    def CheckPalindrome(self,s,start,end):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            count+=1
            start-=1
            end+=1
        
        return count

        