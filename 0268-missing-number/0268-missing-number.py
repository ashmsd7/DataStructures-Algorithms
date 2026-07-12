class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in range(0,len(nums)):
            hash[nums[i]] = 1
        
        for val in range(0,len(nums)+1):
            if val not in hash:
                return val
        return False