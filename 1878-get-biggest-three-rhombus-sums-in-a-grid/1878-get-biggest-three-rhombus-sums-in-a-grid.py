class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        rows, cols = len(grid), len(grid[0])
        sums = set()

        for r in range(rows):
            for c in range(cols):

                # Single cell is a valid rhombus
                sums.add(grid[r][c])

                k = 1

                while r + 2 * k < rows and c - k >= 0 and c + k < cols:

                    total = 0

                    # Top -> Left
                    for i in range(k + 1):
                        total += grid[r + i][c - i]

                    # Top -> Right
                    for i in range(k + 1):
                        total += grid[r + i][c + i]

                    # Left -> Bottom
                    for i in range(k + 1):
                        total += grid[r + k + i][c - k + i]

                    # Right -> Bottom
                    for i in range(k + 1):
                        total += grid[r + k + i][c + k - i]

                    # Each corner was counted twice
                    total -= grid[r][c]           # top
                    total -= grid[r + k][c - k]   # left
                    total -= grid[r + k][c + k]   # right
                    total -= grid[r + 2 * k][c]   # bottom

                    sums.add(total)

                    k += 1

        return sorted(sums, reverse=True)[:3]