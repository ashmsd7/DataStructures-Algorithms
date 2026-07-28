class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hasher = {}
        for i in range (len(s)):
            hasher[s[i]] = hasher.get(s[i],0) + 1

        c = 0
        for key , val in hasher.items():
            if val % 2 !=0:
                c+=1
        if c>1:
            return -1

        sorted_keys = sorted(hasher.keys())

        left = []
        middle = ""

        for char in sorted_keys:
            count = hasher[char]

            if count >= 2:
                left.append(char * (count//2))
            
            if count%2 == 1:
                middle = char
        
        left_str = "".join(left)
        right_str = "".join(left_str[::-1])

        return left_str + middle + right_str



        




        
        
        