"""Unit tests for Distinct Subsequences."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.distinct_subsequences import Solution


class TestDistinctSubsequences(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.numDistinct("caaat", "cat"), 3)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.numDistinct("xxyxy", "xy"), 5)

    def test_repeated_matching_characters_create_multiple_choices(self) -> None:
        self.assertEqual(self.solution.numDistinct("rabbbit", "rabbit"), 3)

    def test_target_longer_than_source_has_no_match(self) -> None:
        self.assertEqual(self.solution.numDistinct("abc", "abcd"), 0)

    def test_no_matching_target_character(self) -> None:
        self.assertEqual(self.solution.numDistinct("abc", "d"), 0)

    def test_maximum_length_source_with_no_match(self) -> None:
        self.assertEqual(self.solution.numDistinct("a" * 1000, "b"), 0)


if __name__ == "__main__":
    unittest.main()
