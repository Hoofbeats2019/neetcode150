"""Unit tests for Contains Duplicate."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_duplicate_in_the_middle(self) -> None:
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test_all_values_are_distinct(self) -> None:
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))

    def test_duplicate_negative_value(self) -> None:
        self.assertTrue(self.solution.containsDuplicate([-1, 4, -1]))

    def test_single_value(self) -> None:
        self.assertFalse(self.solution.containsDuplicate([7]))


if __name__ == "__main__":
    unittest.main()
