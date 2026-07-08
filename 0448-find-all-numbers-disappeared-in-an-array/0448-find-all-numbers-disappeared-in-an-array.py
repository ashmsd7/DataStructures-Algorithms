class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash = {}
        for num in range(1,len(nums)+1):
            hash[num] = 0

        for num in nums:
            hash[num] = 1
        
        res = []

        for key,val in hash.items():
            if val == 0:
                res.append(key)
        return res