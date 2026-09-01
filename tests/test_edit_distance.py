"""Unit tests for Edit Distance."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.edit_distance import Solution


class TestEditDistance(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.minDistance("monkeys", "money"), 2)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.minDistance("neatcdee", "neetcode"), 3)

    def test_both_strings_empty(self) -> None:
        self.assertEqual(self.solution.minDistance("", ""), 0)

    def test_empty_first_string_requires_insertions(self) -> None:
        self.assertEqual(self.solution.minDistance("", "abc"), 3)

    def test_empty_second_string_requires_deletions(self) -> None:
        self.assertEqual(self.solution.minDistance("abc", ""), 3)

    def test_same_length_strings_can_only_need_replacements(self) -> None:
        self.assertEqual(self.solution.minDistance("abc", "xyz"), 3)

    def test_maximum_length_strings(self) -> None:
        self.assertEqual(self.solution.minDistance("a" * 100, "b" * 100), 100)


if __name__ == "__main__":
    unittest.main()
