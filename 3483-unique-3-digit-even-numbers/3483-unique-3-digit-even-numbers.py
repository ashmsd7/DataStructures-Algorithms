class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = set()

        def backtrack(path,seen_indices):
            if len(path) ==3:
                if path[-1]%2 == 0 and path[0]!=0:
                    number = 100 * path[0] + 10* path[1] + path[2]
                    res.add(number)
                return 
            for index in range(len(digits)):
                if index in seen_indices:
                    continue

                if not path and digits[index]== 0:
                    continue
                
                seen_indices.add(index)
                path.append(digits[index])

                backtrack(path,seen_indices)

                path.pop()
                seen_indices.remove(index)
            
        backtrack([],set())
        return len(res)
                    



        