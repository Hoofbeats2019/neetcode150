"""Unit tests for Multiply Strings."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.multiply_strings import Solution


class TestMultiplyStrings(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.multiply("3", "4"), "12")

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.multiply("111", "222"), "24642")

    def test_zero_times_a_number(self) -> None:
        self.assertEqual(self.solution.multiply("0", "123"), "0")

    def test_single_digit_product_with_carry(self) -> None:
        self.assertEqual(self.solution.multiply("9", "9"), "81")

    def test_product_with_internal_zeroes(self) -> None:
        self.assertEqual(self.solution.multiply("101", "10"), "1010")

    def test_product_with_many_carries(self) -> None:
        self.assertEqual(self.solution.multiply("999", "999"), "998001")


if __name__ == "__main__":
    unittest.main()
