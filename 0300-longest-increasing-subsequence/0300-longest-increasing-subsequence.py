class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        indices = [1] * len(nums)
        res = 1

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    indices[i] = max(indices[j] + 1,indices[i])
                    res = max(res,indices[i])
        
        return res
                




        