class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = [0] * n
        left = [0] * n
        right = [0] * n
        Left = 0
        for i in range(n):
            left[i] = Left
            Left+=nums[i]
        
        Right = 0
        for i in range(n-1,-1,-1):
            right[i] = Right
            Right+=nums[i]
        
        for i in range(n):
            sol[i] = abs(left[i] - right[i])

        return sol




        