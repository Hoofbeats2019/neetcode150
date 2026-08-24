"""Unit tests for Palindromic Substrings."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.palindromic_substrings import Solution


class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.countSubstrings("abc"), 3)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.countSubstrings("aaa"), 6)

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.countSubstrings("a"), 1)

    def test_even_length_palindromes(self) -> None:
        self.assertEqual(self.solution.countSubstrings("abba"), 6)

    def test_mixed_odd_and_even_length_palindromes(self) -> None:
        self.assertEqual(self.solution.countSubstrings("aabaa"), 9)

    def test_maximum_length_repeated_characters(self) -> None:
        self.assertEqual(
            self.solution.countSubstrings("a" * 1000),
            500_500,
        )


if __name__ == "__main__":
    unittest.main()
