class Solution:
    def minMoves(self, nums: List[int]) -> int:
        val = max(nums)
        n = len(nums)
        res = 0
        for i in range(n):
            res+= val-nums[i]
        
        return res

        