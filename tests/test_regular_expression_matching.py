"""Unit tests for Regular Expression Matching."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.regular_expression_matching import Solution


class TestRegularExpressionMatching(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertFalse(self.solution.isMatch("aa", ".b"))

    def test_second_worked_example(self) -> None:
        self.assertTrue(self.solution.isMatch("nnn", "n*"))

    def test_third_worked_example(self) -> None:
        self.assertTrue(self.solution.isMatch("xyz", ".*z"))

    def test_star_can_match_zero_preceding_characters(self) -> None:
        self.assertTrue(self.solution.isMatch("b", "a*b"))

    def test_star_can_match_multiple_preceding_characters(self) -> None:
        self.assertTrue(self.solution.isMatch("aab", "c*a*b"))

    def test_dot_star_can_match_an_entire_string(self) -> None:
        self.assertTrue(self.solution.isMatch("abcd", ".*"))

    def test_entire_string_must_match(self) -> None:
        self.assertFalse(self.solution.isMatch("abcd", "d*"))

    def test_overlapping_star_choices_can_fail(self) -> None:
        self.assertFalse(self.solution.isMatch("mississippi", "mis*is*p*."))


if __name__ == "__main__":
    unittest.main()
