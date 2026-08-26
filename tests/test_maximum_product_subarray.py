"""Unit tests for Maximum Product Subarray."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.maximum_product_subarray import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.maxProduct([2, 4, -3, 5]), 8)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.maxProduct([-3, 0, -2]), 0)

    def test_single_positive_element(self) -> None:
        self.assertEqual(self.solution.maxProduct([7]), 7)

    def test_single_negative_element(self) -> None:
        self.assertEqual(self.solution.maxProduct([-7]), -7)

    def test_single_zero(self) -> None:
        self.assertEqual(self.solution.maxProduct([0]), 0)

    def test_two_negative_numbers_make_a_positive_product(self) -> None:
        self.assertEqual(self.solution.maxProduct([-2, -3]), 6)

    def test_previous_minimum_can_become_the_new_maximum(self) -> None:
        self.assertEqual(self.solution.maxProduct([-2, 3, -4]), 24)

    def test_zero_separates_subarrays(self) -> None:
        self.assertEqual(self.solution.maxProduct([-1, -2, 0, -3, -4]), 12)

    def test_odd_number_of_negatives_excludes_one_end(self) -> None:
        self.assertEqual(self.solution.maxProduct([-1, -2, -3]), 6)


if __name__ == "__main__":
    unittest.main()
