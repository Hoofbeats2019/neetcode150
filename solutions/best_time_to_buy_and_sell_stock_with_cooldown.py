"""Best Time to Buy and Sell Stock with Cooldown.

Created: 30 August 2026
Created by: Yanlong Su

You are given an integer array ``prices`` where ``prices[i]`` is the price of
NeetCoin on the ``i``th day. You may buy and sell one NeetCoin multiple times,
but you may own at most one coin at a time. After selling a coin, you cannot
buy another coin on the following day.

Return the maximum profit that can be achieved.

Example 1:
    Input: prices = [1, 3, 4, 0, 4]
    Output: 6
    Explanation: Buy on day 0 and sell on day 1 for profit 2. Buy on day 3
    and sell on day 4 for profit 4, producing total profit 6.

Example 2:
    Input: prices = [1]
    Output: 0

Constraints:
    1 <= len(prices) <= 5000
    0 <= prices[i] <= 1000

Pseudocode:
    maxProfit(prices):
        create an empty memo

        dp(day, holding):
            if day is outside prices, return 0
            if (day, holding) is already in memo, return its stored result

            if holding:
                sell today and continue at day + 2 without a coin
                or keep holding and continue at day + 1
            otherwise:
                buy today and continue at day + 1 holding a coin
                or skip today and continue at day + 1 without a coin

            store and return the larger result

        return dp(day 0, not holding)

Time complexity: O(n)
Space complexity: O(n)
"""

from sys import getrecursionlimit, setrecursionlimit
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the greatest profit while observing the one-day cooldown."""
        setrecursionlimit(max(getrecursionlimit(), len(prices) * 3))
        memo: dict[tuple[int, bool], int] = {}

        def dp(day: int, holding: bool) -> int:
            if day >= len(prices):
                return 0

            state = (day, holding)

            if state in memo:
                return memo[state]

            if holding:
                sell_today = prices[day] + dp(day + 2, False)
                keep_holding = dp(day + 1, True)
                memo[state] = max(sell_today, keep_holding)
            else:
                buy_today = -prices[day] + dp(day + 1, True)
                skip_today = dp(day + 1, False)
                memo[state] = max(buy_today, skip_today)

            return memo[state]

        return dp(0, False)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().maxProfit([1, 3, 4, 0, 4]) == 6


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().maxProfit([1]) == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
