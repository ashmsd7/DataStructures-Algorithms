class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        MaxSum = 0
        currSum = nums[0]

        if len(nums) == 1 or nums[1]-nums[0]!=1:
            MaxSum = nums[0]
        else:   
            for i in range(len(nums)-1):
                if nums[i+1] - nums[i] == 1:
                    currSum+=nums[i+1]
                else:
                    MaxSum = max(MaxSum,currSum)
                    currSum = 0
            MaxSum = max(MaxSum, currSum)
        while MaxSum in nums:
            MaxSum = MaxSum + 1

        return MaxSum
        
                