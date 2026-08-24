"""Unit tests for Longest Palindromic Substring."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.longest_palindromic_substring import Solution


class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        result = self.solution.longestPalindrome("ababd")
        self.assertIn(result, {"aba", "bab"})

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.longestPalindrome("abbc"), "bb")

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.longestPalindrome("7"), "7")

    def test_whole_string_is_a_palindrome(self) -> None:
        self.assertEqual(self.solution.longestPalindrome("racecar"), "racecar")

    def test_longest_palindrome_is_at_an_edge(self) -> None:
        self.assertEqual(self.solution.longestPalindrome("abac"), "aba")

    def test_maximum_length_palindrome(self) -> None:
        s = "a" * 1000
        self.assertEqual(self.solution.longestPalindrome(s), s)

    def test_long_runs_separated_by_different_characters(self) -> None:
        s = "j" * 500 + "kl" + "j" * 498
        self.assertEqual(self.solution.longestPalindrome(s), "j" * 500)


if __name__ == "__main__":
    unittest.main()
