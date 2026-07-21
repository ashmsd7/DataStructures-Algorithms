class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float ('inf')
        curr_sum = 0
        
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        length = l 
        x = 0
        for x in range(0,len(nums)):
            for length in range(l,r+1):
                y = length + x -1
                if y >= len(nums):
                    break
                curr_sum = prefix[y] - prefix[x-1] if x>0 else prefix[y]
                if curr_sum > 0:
                    min_sum = min(curr_sum,min_sum)
        return -1 if min_sum == float('inf') else min_sum
