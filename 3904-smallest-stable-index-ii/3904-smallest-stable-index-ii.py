class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        sol = [0]*len(nums)
        sol[-1] = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            sol[i] = min(nums[i],sol[i+1])
        
        maximum = nums[0]
        for i in range(len(nums)):
            maximum = max(maximum,nums[i])
            if maximum - sol[i]<=k:
                return i
        
        return -1
        
        