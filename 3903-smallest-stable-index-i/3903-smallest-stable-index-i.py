class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0

        n = len(nums)

        for i in range(n):
            Max_el = max(nums[0:i+1])
            Min_el = min(nums[i:n])
            if Max_el - Min_el <= k:
                return i
        return -1



        