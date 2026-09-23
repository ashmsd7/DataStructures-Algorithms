class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        arr_sum = sum(nums)
        target = arr_sum - x
        n = len(nums)

        prefix = [0] * (n+1)

        hasher = {0:0}
        max_len = 0

        if target < 0 :
            return -1
        if target == 0:
            return n

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(n+1):
            needed = prefix[i] - target
            if needed in hasher:
                curr_len = i - hasher[needed]
                max_len = max(max_len , curr_len)

            if prefix[i] not in hasher:
                hasher[prefix[i]] = i
            
        if max_len == 0:
            return -1
        
        return n - max_len

