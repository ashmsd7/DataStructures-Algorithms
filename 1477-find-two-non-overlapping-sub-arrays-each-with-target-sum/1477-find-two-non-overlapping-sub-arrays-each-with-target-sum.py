class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = float('inf')
        seen = {0: 0}
        curr_sum = 0
        n = len(arr)

        best = [float('inf')] * (n + 1)

        for i in range(1, n + 1):

            curr_sum += arr[i - 1]

            # Carry previous best forward
            best[i] = best[i - 1]

            needed = curr_sum - target

            if needed in seen:
                start = seen[needed]
                length = i - start


                if best[start] != float('inf'):
                    ans = min(ans, length + best[start])

                best[i] = min(best[i], length)

            seen[curr_sum] = i

        return -1 if ans == float('inf') else ans