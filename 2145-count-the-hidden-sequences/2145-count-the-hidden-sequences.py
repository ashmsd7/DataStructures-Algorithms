class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low = lower
        high = upper
        prefix = 0

        for diff in differences:
            prefix+=diff

            low = max(low,lower-prefix)
            high = min(high,upper-prefix)

            if low > high:
                return 0
        
        return high - low + 1
        