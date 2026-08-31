"""Distinct Subsequences.

Created: 31 August 2026
Created by: Yanlong Su

Given two strings ``s`` and ``t`` consisting of English letters, return the
number of distinct subsequences of ``s`` that equal ``t``.

Example 1:
    Input: s = "caaat", t = "cat"
    Output: 3
    Explanation: The three choices are (c)aa(at), (c)a(a)a(t), and (ca)aa(t).

Example 2:
    Input: s = "xxyxy", t = "xy"
    Output: 5

Constraints:
    1 <= len(s), len(t) <= 1000
    s and t consist of English letters.

Pseudocode:
    numDistinct(s, t):
        create an empty memo

        dfs(i, j):
            if j reaches the end of t:
                return 1
            if i reaches the end of s:
                return 0
            if (i, j) has a memoized result:
                return it

            ways = dfs(i + 1, j)
            if s[i] equals t[j]:
                ways += dfs(i + 1, j + 1)

            store ways for (i, j)
            return ways

        return dfs(0, 0)

Time complexity: O(len(s) * len(t))
Space complexity: O(len(s) * len(t))
"""

import sys


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """Return the number of subsequences of ``s`` equal to ``t``."""
        required_limit = len(s) + len(t) + 100

        if sys.getrecursionlimit() < required_limit:
            sys.setrecursionlimit(required_limit)

        memo: dict[tuple[int, int], int] = {}

        def dfs(source_index: int, target_index: int) -> int:
            if target_index == len(t):
                return 1

            if source_index == len(s):
                return 0

            state = (source_index, target_index)

            if state in memo:
                return memo[state]

            ways = dfs(source_index + 1, target_index)

            if s[source_index] == t[target_index]:
                ways += dfs(source_index + 1, target_index + 1)

            memo[state] = ways
            return ways

        return dfs(0, 0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().numDistinct("caaat", "cat") == 3


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().numDistinct("xxyxy", "xy") == 5


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
