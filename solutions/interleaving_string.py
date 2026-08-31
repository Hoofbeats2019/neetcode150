"""Interleaving String.

Created: 31 August 2026
Created by: Yanlong Su

Given three strings ``s1``, ``s2``, and ``s3``, return ``True`` when ``s3``
is an interleaving of ``s1`` and ``s2``. An interleaving preserves the
relative order of characters from each input string.

Example 1:
    Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"
    Output: True
    Explanation: Split s1 into ["aa", "aa"] and leave s2 as "bbbb".

Example 2:
    Input: s1 = "", s2 = "", s3 = ""
    Output: True

Example 3:
    Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"
    Output: False

Constraints:
    0 <= len(s1), len(s2) <= 100
    0 <= len(s3) <= 200
    s1, s2, and s3 contain only lowercase English letters.

Pseudocode:
    isInterleave(s1, s2, s3):
        if len(s1) + len(s2) does not equal len(s3):
            return false

        create an empty memo

        dfs(i, j):
            k = i + j
            if i and j both reach the ends of s1 and s2:
                return true
            if (i, j) is memoized:
                return its result

            try consuming s3[k] from s1 when the characters match
            if that did not succeed, try consuming s3[k] from s2 when they match
            memoize and return whether either choice succeeds

        return dfs(0, 0)

Time complexity: O(len(s1) * len(s2))
Space complexity: O(len(s1) * len(s2))
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Return whether ``s3`` preserves the character orders of ``s1`` and ``s2``."""
        if len(s1) + len(s2) != len(s3):
            return False

        memo: dict[tuple[int, int], bool] = {}

        def dfs(index1: int, index2: int) -> bool:
            if index1 == len(s1) and index2 == len(s2):
                return True

            state = (index1, index2)

            if state in memo:
                return memo[state]

            index3 = index1 + index2
            can_interleave = False

            if index1 < len(s1) and s1[index1] == s3[index3]:
                can_interleave = dfs(index1 + 1, index2)

            if (
                not can_interleave
                and index2 < len(s2)
                and s2[index2] == s3[index3]
            ):
                can_interleave = dfs(index1, index2 + 1)

            memo[state] = can_interleave
            return can_interleave

        return dfs(0, 0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().isInterleave("aaaa", "bbbb", "aabbbbaa") is True


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().isInterleave("", "", "") is True


def test_example_3() -> None:
    """Run the third worked example."""
    assert Solution().isInterleave("abc", "xyz", "abxzcy") is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
