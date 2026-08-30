"""Longest Common Subsequence.

Created: 30 August 2026
Created by: Yanlong Su

Given two strings ``text1`` and ``text2``, return the length of their
longest common subsequence. Return ``0`` when they have no common
subsequence.

A subsequence is formed by deleting zero or more characters without changing
the relative order of the characters that remain.

Example 1:
    Input: text1 = "cat", text2 = "crabt"
    Output: 3
    Explanation: The longest common subsequence is "cat".

Example 2:
    Input: text1 = "abcd", text2 = "abcd"
    Output: 4

Example 3:
    Input: text1 = "abcd", text2 = "efgh"
    Output: 0

Constraints:
    1 <= len(text1), len(text2) <= 1000
    text1 and text2 contain only lowercase English characters.

Pseudocode:
    longestCommonSubsequence(text1, text2):
        create an empty memo

        dp(i, j):
            if i reaches the end of text1 or j reaches the end of text2:
                return 0
            if (i, j) has a memoized result:
                return it

            if text1[i] equals text2[j]:
                result = 1 + dp(i + 1, j + 1)
            otherwise:
                result = maximum of dp(i + 1, j) and dp(i, j + 1)

            store result for (i, j)
            return result

        return dp(0, 0)

Time complexity: O(len(text1) * len(text2))
Space complexity: O(len(text1) * len(text2))
"""

import sys


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return the length of the longest subsequence shared by both strings."""
        required_limit = 2 * (len(text1) + len(text2)) + 100

        if sys.getrecursionlimit() < required_limit:
            sys.setrecursionlimit(required_limit)

        memo: dict[tuple[int, int], int] = {}

        def dp(index1: int, index2: int) -> int:
            if index1 == len(text1) or index2 == len(text2):
                return 0

            state = (index1, index2)

            if state in memo:
                return memo[state]

            if text1[index1] == text2[index2]:
                result = 1 + dp(index1 + 1, index2 + 1)
            else:
                skip_text1 = dp(index1 + 1, index2)
                skip_text2 = dp(index1, index2 + 1)
                result = max(skip_text1, skip_text2)

            memo[state] = result
            return result

        return dp(0, 0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().longestCommonSubsequence("cat", "crabt") == 3


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().longestCommonSubsequence("abcd", "abcd") == 4


def test_example_3() -> None:
    """Run the third worked example."""
    assert Solution().longestCommonSubsequence("abcd", "efgh") == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
