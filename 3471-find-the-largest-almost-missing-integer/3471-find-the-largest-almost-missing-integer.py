class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}

        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]

            for num in set(window):
                freq[num] = freq.get(num, 0) + 1

        ans = -1

        for num, count in freq.items():
            if count == 1:
                ans = max(ans, num)

        return ans