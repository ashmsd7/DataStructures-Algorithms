class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum -= num
        
        for num in range(len(nums)+1):
            total_sum += num
        return total_sum
        