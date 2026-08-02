class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        sol  = []
        n = len(nums)
        def backtrack():
            if len(path) == n:
                sol.append(path[:])
                return
            for x in nums:
                if x not in path:
                    path.append(x)
                    backtrack()
                    path.pop()
        backtrack()
        return sol