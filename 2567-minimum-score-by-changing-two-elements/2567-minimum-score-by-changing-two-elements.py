class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if n==3:
            return 0

        #two largest -> 

        two_l = nums[n-3]-nums[0]
        
        #two smallest ->

        two_s = nums[n-1] - nums[2]

        #one small and one large

        one_s_l = nums[n-2] - nums[1]

        return min(one_s_l,two_s,two_l)
        