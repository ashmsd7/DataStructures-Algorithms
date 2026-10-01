class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        from collections import Counter
        from functools import cache
        import math

        MOD = 10**9 + 7

        Count = Counter(int(ch) for ch in num)
        total = sum(int(ch) for ch in num)
        n = len(num)

        # Odd total sum can never be split equally
        if total % 2:
            return 0

        # 0-based indexing:
        # even indices = ceil(n / 2)
        # odd indices  = floor(n / 2)
        even = (n + 1) // 2
        odd = n // 2

        @cache
        def dfs(digit, even, odd, balance_sum):
            if even == 0 and odd == 0 and balance_sum == 0:
                return 1

            if digit < 0 or even < 0 or odd < 0 or balance_sum < 0:
                return 0

            res = 0
            cnt = Count[digit]

            # j copies of this digit go into odd positions
            for j in range(cnt + 1):
                even_used = cnt - j

                ways = (
                    math.comb(odd, j)
                    * math.comb(even, even_used)
                )

                res += ways * dfs(
                    digit - 1,
                    even - even_used,
                    odd - j,
                    balance_sum - digit * j
                )

            return res % MOD

        return dfs(9, even, odd, total // 2)