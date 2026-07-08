class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in range (0,len(nums)):
            if nums[i] in hash:
                return True
            else :
                hash[nums[i]] = 'k'
        return False

        