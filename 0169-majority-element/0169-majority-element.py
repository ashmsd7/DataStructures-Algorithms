class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for i in range(0,len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]]+=1
        max_val = 0
        for key,val in hash.items():
            if val > max_val:
                max_val = val

        for key,val in hash.items():
            if val == max_val:
                return key
    
        