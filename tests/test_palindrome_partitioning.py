"""Unit tests for Palindrome Partitioning.

Test pseudocode:
    for each input string:
        request every palindrome partition
        normalize the partition ordering
        verify the expected partitions are returned exactly once

    for direct edge cases:
        verify a single character forms one partition
        verify a whole-string palindrome is included
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.palindrome_partitioning import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertPartitionsEqual(
        self,
        actual: list[list[str]],
        expected: list[list[str]],
    ) -> None:
        normalized_actual = sorted(tuple(partition) for partition in actual)
        normalized_expected = sorted(tuple(partition) for partition in expected)
        self.assertEqual(normalized_actual, normalized_expected)

    def test_multiple_partitions(self) -> None:
        actual = self.solution.partition("aab")
        self.assertPartitionsEqual(
            actual,
            [["a", "a", "b"], ["aa", "b"]],
        )

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.partition("a"), [["a"]])

    def test_whole_string_palindrome(self) -> None:
        actual = self.solution.partition("aba")
        self.assertPartitionsEqual(
            actual,
            [["a", "b", "a"], ["aba"]],
        )

    def test_repeated_characters(self) -> None:
        actual = self.solution.partition("aaa")
        self.assertPartitionsEqual(
            actual,
            [
                ["a", "a", "a"],
                ["a", "aa"],
                ["aa", "a"],
                ["aaa"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
