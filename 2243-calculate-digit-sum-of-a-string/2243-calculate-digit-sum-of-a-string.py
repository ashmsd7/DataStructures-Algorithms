class Solution:
    def digitSum(self, s: str, k: int) -> str:
        #keep looping and applying operations until size of s is less than OR equal to k

        while len(s)>k:
            n = len(s)
            string = ""
            for i in range(0,n,k):
                sub = s[i:i+k]
                res = 0
                for char in sub:
                    res+=int(char)
                string+= str(res)
            s=string
        
        return s
                




        