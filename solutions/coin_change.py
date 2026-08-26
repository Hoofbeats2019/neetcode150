"""Coin Change.

Created: 26 August 2026
Created by: Yanlong Su

You are given an integer array ``coins`` representing coins of different
denominations and an integer ``amount`` representing a target amount of money.

Return the fewest number of coins needed to make up the exact target amount.
If it is impossible to make up the amount, return ``-1``. You may use an
unlimited number of each coin.

Example 1:
    Input: coins = [1, 5, 10], amount = 12
    Output: 3
    Explanation: ``12 = 10 + 1 + 1``.

Example 2:
    Input: coins = [2], amount = 3
    Output: -1
    Explanation: An amount of 3 cannot be made using coins of value 2.

Example 3:
    Input: coins = [1], amount = 0
    Output: 0
    Explanation: Choosing zero coins is a valid way to make up zero.

Constraints:
    1 <= len(coins) <= 10
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10000

Pseudocode:
    coinChange(coins, amount):
        create an empty memo

        fewestCoins(remaining):
            if remaining is 0, return 0
            if remaining is negative, return -1
            if remaining is already in memo, return its stored result

            set the minimum result to an unreachable sentinel

            for each coin:
                solve the smaller problem for remaining - coin
                if that smaller problem is possible:
                    minimize the result using smaller result + 1

            store -1 if no smaller problem was possible
            otherwise store the minimum result
            return the stored result

        return fewestCoins(amount)

Time complexity: O(amount * len(coins))
Space complexity: O(amount)
"""

import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Return the fewest coins needed to make ``amount`` exactly."""
        sys.setrecursionlimit(
            max(sys.getrecursionlimit(), amount + 100)
        )

        memo: dict[int, int] = {}
        unreachable = amount + 1

        def fewest_coins(remaining: int) -> int:
            if remaining == 0:
                return 0

            if remaining < 0:
                return -1

            if remaining in memo:
                return memo[remaining]

            minimum_coins = unreachable

            for coin in coins:
                smaller_result = fewest_coins(remaining - coin)

                if smaller_result != -1:
                    minimum_coins = min(
                        minimum_coins,
                        smaller_result + 1,
                    )

            if minimum_coins == unreachable:
                memo[remaining] = -1
            else:
                memo[remaining] = minimum_coins

            return memo[remaining]

        return fewest_coins(amount)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().coinChange([1, 5, 10], 12) == 3


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().coinChange([2], 3) == -1


def test_example_3() -> None:
    """Run the third worked example."""
    assert Solution().coinChange([1], 0) == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
