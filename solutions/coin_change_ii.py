"""Coin Change II.

Created: 30 August 2026
Created by: Yanlong Su

You are given an integer array ``coins`` representing coins of different
denominations and an integer ``amount`` representing a target amount of money.

Return the number of distinct combinations of coins that total ``amount``.
Return ``0`` when it is impossible to make the amount. Each coin denomination
may be used an unlimited number of times, and every value in ``coins`` is
unique.

Example 1:
    Input: amount = 4, coins = [1, 2, 3]
    Output: 4
    Explanation: The combinations are ``1 + 1 + 1 + 1``, ``1 + 1 + 2``,
    ``2 + 2``, and ``1 + 3``.

Example 2:
    Input: amount = 7, coins = [2, 4]
    Output: 0

Constraints:
    1 <= len(coins) <= 100
    1 <= coins[i] <= 5000
    0 <= amount <= 5000

Pseudocode:
    change(amount, coins):
        create an empty memo

        countCombinations(index, remainingAmount):
            if remainingAmount is 0, return 1
            if index reaches the end of coins, return 0
            if (index, remainingAmount) is in memo, return its result

            combinations = countCombinations(index + 1, remainingAmount)

            if coins[index] fits in remainingAmount:
                combinations += countCombinations(
                    index,
                    remainingAmount - coins[index]
                )

            store combinations in memo
            return combinations

        return countCombinations(0, amount)

Time complexity: O(len(coins) * amount)
Space complexity: O(len(coins) * amount)
"""

import sys
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """Return the number of unique coin combinations totaling ``amount``."""
        sys.setrecursionlimit(
            max(sys.getrecursionlimit(), amount + len(coins) + 100)
        )

        memo: dict[tuple[int, int], int] = {}

        def count_combinations(index: int, remaining_amount: int) -> int:
            if remaining_amount == 0:
                return 1

            if index == len(coins):
                return 0

            state = (index, remaining_amount)

            if state in memo:
                return memo[state]

            combinations = count_combinations(index + 1, remaining_amount)

            if coins[index] <= remaining_amount:
                combinations += count_combinations(
                    index,
                    remaining_amount - coins[index],
                )

            memo[state] = combinations
            return combinations

        return count_combinations(0, amount)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().change(4, [1, 2, 3]) == 4


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().change(7, [2, 4]) == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
