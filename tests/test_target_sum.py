"""Unit tests for Target Sum."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.target_sum import Solution


class TestTargetSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.findTargetSumWays([2, 2, 2], 2), 3)

    def test_duplicate_values_have_distinct_sign_assignments(self) -> None:
        self.assertEqual(self.solution.findTargetSumWays([1, 1], 0), 2)

    def test_zero_has_two_sign_choices(self) -> None:
        self.assertEqual(self.solution.findTargetSumWays([0], 0), 2)

    def test_multiple_zeros_multiply_the_number_of_ways(self) -> None:
        self.assertEqual(self.solution.findTargetSumWays([0, 0, 1], 1), 4)

    def test_unreachable_target_returns_zero(self) -> None:
        self.assertEqual(self.solution.findTargetSumWays([1, 2, 3], 7), 0)

    def test_negative_target(self) -> None:
        self.assertEqual(self.solution.findTargetSumWays([1, 2, 1], -2), 2)

    def test_maximum_length_with_zeros(self) -> None:
        self.assertEqual(
            self.solution.findTargetSumWays([0] * 20, 0),
            2**20,
        )


if __name__ == "__main__":
    unittest.main()
