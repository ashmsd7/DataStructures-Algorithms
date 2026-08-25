class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp = k
        while temp in nums:
            temp+=k
        return temp 
        