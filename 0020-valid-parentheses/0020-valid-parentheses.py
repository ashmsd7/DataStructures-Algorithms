class Solution:
    def isValid(self, s: str) -> bool:

        matching = {')':'(' , '}':'{' , ']' : '['}

        stacker = []

        for char in s:
            if char in matching.values():
                stacker.append(char)
            elif char in matching:
                if not stacker or matching[char]!=stacker.pop():
                    return False
        
        return len(stacker) == 0
