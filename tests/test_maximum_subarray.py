"""Unit tests for Maximum Subarray."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.maximum_subarray import Solution


class TestMaximumSubarray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(
            self.solution.maxSubArray([2, -3, 4, -2, 2, 1, -1, 4]), 8
        )

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.maxSubArray([-1]), -1)

    def test_all_negative_numbers(self) -> None:
        self.assertEqual(self.solution.maxSubArray([-5, -2, -7]), -2)

    def test_restarts_after_a_negative_prefix(self) -> None:
        self.assertEqual(self.solution.maxSubArray([-2, 1]), 1)

    def test_full_array_is_the_best_subarray(self) -> None:
        self.assertEqual(self.solution.maxSubArray([1, 2, 3]), 6)

    def test_zero_can_be_the_largest_sum(self) -> None:
        self.assertEqual(self.solution.maxSubArray([-2, 0, -1]), 0)


if __name__ == "__main__":
    unittest.main()
