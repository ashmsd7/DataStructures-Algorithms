class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = 0
        res+=nums[0]
        nums.remove(nums[0])            

        for _ in range(2):
            min_idx = nums.index(min(nums))
            res+= nums[min_idx]
            nums.remove(nums[min_idx])
        
        return res




        