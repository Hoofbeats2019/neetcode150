"""Best Time to Buy and Sell Stock.

Return the greatest profit from one buy followed by one later sell.
"""

from typing import List


class Solution:
    """Keep the cheapest earlier price while scanning possible sale prices."""

    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        best = 0
        for price in prices:
            lowest = min(lowest, price)
            best = max(best, price - lowest)
        return best


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    print("The worked example passed.")
