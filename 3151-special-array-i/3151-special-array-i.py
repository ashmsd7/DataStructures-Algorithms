class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        #Can do with bit manipulation. But lets just traverse the array normally and check

        n = len(nums)
        if len(nums) == 0 or len(nums) == 1:
            return True
        for i in range(0,n-1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False
        
        return True


        