class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = str(nums[i])
            curr_sum = 0
            for char in val:
                curr_sum+= int(char)
            
            if curr_sum == i:
                return i
        
        return -1
        