class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        temp = word
        res = 0
        while temp:
            temp = temp[k:]
            res+=1
            if temp == word[:len(temp)]:
                return res
        return res