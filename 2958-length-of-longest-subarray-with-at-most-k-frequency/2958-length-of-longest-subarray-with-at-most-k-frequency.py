class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hasher = {}
        l = 0
        max_len = 0

        for r in range(len(nums)):
            hasher[nums[r]] = hasher.get(nums[r],0) + 1
            while hasher[nums[r]] > k:
                hasher[nums[l]]-=1
                l+=1
            max_len = max(max_len,r-l+1)
        
        return max_len

                
        