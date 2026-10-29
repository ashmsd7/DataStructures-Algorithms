class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = -1

        for i in range(n - 1):
            if nums[i + 1] - nums[i] != 1:
                continue

            curr = 2

            for j in range(i + 2, n):
                expected = -1 if curr % 2 == 0 else 1

                if nums[j] - nums[j - 1] == expected:
                    curr += 1
                    max_len = max(max_len, curr)
                else:
                    break

            max_len = max(max_len, 2)

        return max_len