class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        nums = sorted(x*x for x in nums)
        
        return sum(nums[n//2:]) - sum(nums[:n//2])

        