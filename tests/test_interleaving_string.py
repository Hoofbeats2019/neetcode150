"""Unit tests for Interleaving String."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.interleaving_string import Solution


class TestInterleavingString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(self.solution.isInterleave("aaaa", "bbbb", "aabbbbaa"))

    def test_second_worked_example(self) -> None:
        self.assertTrue(self.solution.isInterleave("", "", ""))

    def test_third_worked_example(self) -> None:
        self.assertFalse(self.solution.isInterleave("abc", "xyz", "abxzcy"))

    def test_matching_characters_can_require_trying_both_sources(self) -> None:
        self.assertTrue(self.solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_matching_characters_with_no_valid_interleaving(self) -> None:
        self.assertFalse(self.solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_length_mismatch_is_not_an_interleaving(self) -> None:
        self.assertFalse(self.solution.isInterleave("a", "b", "abx"))

    def test_one_empty_source_string(self) -> None:
        self.assertTrue(self.solution.isInterleave("", "abc", "abc"))


if __name__ == "__main__":
    unittest.main()
