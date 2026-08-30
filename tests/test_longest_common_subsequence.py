"""Unit tests for Longest Common Subsequence."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.longest_common_subsequence import Solution


class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.longestCommonSubsequence("cat", "crabt"), 3)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.longestCommonSubsequence("abcd", "abcd"), 4)

    def test_third_worked_example(self) -> None:
        self.assertEqual(self.solution.longestCommonSubsequence("abcd", "efgh"), 0)

    def test_matching_characters_need_not_be_contiguous(self) -> None:
        self.assertEqual(self.solution.longestCommonSubsequence("abcde", "ace"), 3)

    def test_repeated_characters(self) -> None:
        self.assertEqual(self.solution.longestCommonSubsequence("aab", "azab"), 3)

    def test_maximum_length_strings_with_no_common_subsequence(self) -> None:
        self.assertEqual(
            self.solution.longestCommonSubsequence("a" * 1000, "b" * 1000),
            0,
        )


if __name__ == "__main__":
    unittest.main()
