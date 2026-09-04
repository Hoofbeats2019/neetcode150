"""Unit tests for Plus One."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.plus_one import Solution


class TestPlusOne(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.plusOne([1, 2, 3, 4]), [1, 2, 3, 5])

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_single_digit_without_carry(self) -> None:
        self.assertEqual(self.solution.plusOne([5]), [6])

    def test_single_digit_with_carry(self) -> None:
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_carry_stops_before_most_significant_digit(self) -> None:
        self.assertEqual(self.solution.plusOne([2, 9, 9]), [3, 0, 0])


if __name__ == "__main__":
    unittest.main()
