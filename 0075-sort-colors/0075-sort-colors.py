class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        hash = {}

        for val in nums:
            hash[val] = hash.get(val,0) + 1
    

        idx = 0
        for color in (0,1,2):
            for _ in range(hash.get(color,0)):
                nums[idx] = color
                idx+=1
