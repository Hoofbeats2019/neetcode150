"""Unit tests for Non-Cyclical Number."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.non_cyclical_number import Solution


class TestNonCyclicalNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(self.solution.isHappy(100))

    def test_second_worked_example(self) -> None:
        self.assertFalse(self.solution.isHappy(101))

    def test_one_is_non_cyclical(self) -> None:
        self.assertTrue(self.solution.isHappy(1))

    def test_single_digit_cycle_member(self) -> None:
        self.assertFalse(self.solution.isHappy(4))

    def test_largest_allowed_input(self) -> None:
        self.assertTrue(self.solution.isHappy(1000))


if __name__ == "__main__":
    unittest.main()
