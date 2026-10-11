class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!= len(s.split()):
            return False
        
        arr2 = s.split()
        arr1 = list(pattern)

        l2w = {}
        w2l = {}

        for letter , word in zip(arr1,arr2):
            if letter in l2w and l2w[letter]!=word:
                return False
            
            if word in w2l and w2l[word]!=letter:
                return False
            
            l2w[letter] = word
            w2l[word] = letter

        return True

        