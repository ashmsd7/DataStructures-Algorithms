class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        count = Counter()

        for arr in nums:
            count.update(set(arr))
        
        n = len(nums)
        return sorted(list(x for x,freq in count.items() if freq==n))

        