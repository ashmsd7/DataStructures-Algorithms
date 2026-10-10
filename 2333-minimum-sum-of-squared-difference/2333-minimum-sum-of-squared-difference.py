class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:

        absolute = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if k >= sum(absolute):
            return 0

        # Can we reduce every difference to at most 'mid'
        # using at most k operations?
        def possible(mid):
            operations = 0

            for d in absolute:
                if d > mid:
                    operations += d - mid

            return operations <= k

        left, right = 0, max(absolute)

        while left < right:
            mid = (left + right) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        # 'left' is the smallest achievable maximum difference.
        threshold = left

        # Reduce every difference above the threshold.
        remaining = k
        for d in absolute:
            if d > threshold:
                remaining -= d - threshold

        # All differences are now at most threshold.
        # Spend leftover operations by reducing threshold values.
        res = 0
        for d in absolute:
            if d > threshold:
                d = threshold
            res += d * d

        # Each leftover operation reduces one threshold value
        # from threshold to threshold - 1.
        res -= remaining * (2 * threshold - 1)

        return res