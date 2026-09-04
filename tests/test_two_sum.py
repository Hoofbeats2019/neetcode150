"""Unit tests for Two Sum."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_worked_examples(self) -> None:
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_reuses_equal_values_at_different_indexes(self) -> None:
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_negative_numbers(self) -> None:
        self.assertEqual(self.solution.twoSum([-3, 4, 3, 90], 0), [0, 2])


if __name__ == "__main__":
    unittest.main()
