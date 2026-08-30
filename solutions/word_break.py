"""Word Break.

Created: 30 August 2026
Created by: Yanlong Su

Given a string ``s`` and a dictionary of strings ``wordDict``, return ``True``
if ``s`` can be segmented into a space-separated sequence of dictionary words.

Words in the dictionary may be reused an unlimited number of times. All words
in ``wordDict`` are unique.

Example 1:
    Input: s = "neetcode", wordDict = ["neet", "code"]
    Output: True
    Explanation: ``neetcode`` can be split into ``neet`` and ``code``.

Example 2:
    Input: s = "applepenapple", wordDict = ["apple", "pen", "ape"]
    Output: True
    Explanation: ``applepenapple`` can be split into ``apple``, ``pen``, and
    ``apple``. Words may be reused, and not every dictionary word must be used.

Example 3:
    Input: s = "catsincars", wordDict = ["cats", "cat", "sin", "in", "car"]
    Output: False

Constraints:
    1 <= len(s) <= 200
    1 <= len(wordDict) <= 100
    1 <= len(wordDict[i]) <= 20
    s and wordDict[i] contain only lowercase English letters

Pseudocode:
    wordBreak(s, wordDict):
        create an empty memo

        canBreak(start):
            if start is at the end of s, return true
            if start is already in memo, return its stored result

            for each word in wordDict:
                if s starting at start has word as a prefix:
                    move nextStart past that word
                    if canBreak(nextStart) is true:
                        store true for start
                        return true

            store false for start after every word has failed
            return false

        return canBreak(0)

Time complexity: O(n * m * L)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Return whether ``s`` can be segmented into dictionary words."""
        memo: dict[int, bool] = {}

        def can_break(start: int) -> bool:
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for word in wordDict:
                if s.startswith(word, start):
                    next_start = start + len(word)

                    if can_break(next_start):
                        memo[start] = True
                        return memo[start]

            memo[start] = False
            return memo[start]

        return can_break(0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().wordBreak("neetcode", ["neet", "code"]) is True


def test_example_2() -> None:
    """Run the second worked example."""
    assert (
        Solution().wordBreak(
            "applepenapple",
            ["apple", "pen", "ape"],
        )
        is True
    )


def test_example_3() -> None:
    """Run the third worked example."""
    assert (
        Solution().wordBreak(
            "catsincars",
            ["cats", "cat", "sin", "in", "car"],
        )
        is False
    )


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
