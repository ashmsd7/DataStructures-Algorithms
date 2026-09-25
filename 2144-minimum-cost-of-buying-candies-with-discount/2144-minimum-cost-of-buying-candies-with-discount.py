class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()

        total = 0
        n = len(cost)

        # Pay for leftovers that cannot form a group of 3
        start = n % 3
        for i in range(start):
            total += cost[i]

        # Process complete groups from the expensive end
        i = n - 1

        while i >= start:
            # Three items: cheapest is free
            total += cost[i] + cost[i - 1]
            i -= 3

        return total