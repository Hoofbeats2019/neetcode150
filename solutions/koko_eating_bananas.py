"""Koko Eating Bananas.

Created: 2 August 2026
Created by: Yanlong Su

You are given an integer array ``piles`` where ``piles[i]`` is the number of
bananas in the ith pile. You are also given an integer ``h``, which represents
the number of hours available to eat all the bananas.

Return the minimum integer eating rate ``k`` that finishes all the bananas
within ``h`` hours.

Example 1:
    Input: piles = [1, 4, 3, 2], h = 9
    Output: 2

Example 2:
    Input: piles = [25, 10, 23, 4], h = 4
    Output: 25

Executable examples:
    >>> solution = Solution()
    >>> solution.minEatingSpeed([1, 4, 3, 2], 9)
    2
    >>> solution.minEatingSpeed([25, 10, 23, 4], 4)
    25

Constraints:
    1 <= piles.length <= 1000
    piles.length <= h <= 1000000
    1 <= piles[i] <= 1000000000
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower < upper:
            middle = lower + (upper - lower) // 2

            total_hours = 0
            for pile in piles:
                total_hours += (pile + middle - 1) // middle

            if total_hours > h:
                lower = middle + 1
            else:
                upper = middle

        return lower


def test_example_1() -> None:
    solution = Solution()
    actual = solution.minEatingSpeed([1, 4, 3, 2], 9)
    expected = 2
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.minEatingSpeed([25, 10, 23, 4], 4)
    expected = 25
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
