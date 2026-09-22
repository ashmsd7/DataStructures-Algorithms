class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        res = 1
        nums.sort()
        start = 0

        for i in range(1,len(nums)):
            if nums[i] - nums[start] > k:
                res+=1
                start = i

        return res
            

            


        