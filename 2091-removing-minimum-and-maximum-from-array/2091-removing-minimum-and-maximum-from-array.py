class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        n= len(nums)
        
        minimum = nums.index(min(nums))
        maximum = nums.index(max(nums))

        left = max(minimum,maximum) + 1

        right = n - min(minimum,maximum)

        middle = min(minimum,maximum) + 1 + n -max(maximum,minimum)

        return min(left,right,middle)

