class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        Hasher = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        def backtrack(index, currentString):
            if len(currentString) == len(digits):
                res.append(currentString)
                return
            
            for char in Hasher[digits[index]]:
                backtrack(index+1,currentString + char)
        
        backtrack(0,"")
        return res