class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        Set = set()
        for i in range(len(digits)):
            if digits[i]!=0:
                for j in range(len(digits)):
                    for k in range(len(digits)):
                        if digits[k]%2==0 and i!=k and i!=j and j!=k:
                            number = digits[i] * 100 + digits[j] * 10 + digits[k]

                            if number not in Set:
                                Set.add(number)
        
        return len(Set)

            
        