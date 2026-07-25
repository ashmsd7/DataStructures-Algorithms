class Solution:
    def maxProduct(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        nums.sort(reverse=True)
        return nums[0] * nums[1] 