class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for f in count.values():
            if f>2:
                return False
        
        return True

        