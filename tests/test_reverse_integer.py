"""Unit tests for Reverse Integer."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.reverse(1234), 4321)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.reverse(-1234), -4321)

    def test_overflow_returns_zero(self) -> None:
        self.assertEqual(self.solution.reverse(1234236467), 0)

    def test_zero_remains_zero(self) -> None:
        self.assertEqual(self.solution.reverse(0), 0)

    def test_trailing_zero_is_not_preserved(self) -> None:
        self.assertEqual(self.solution.reverse(120), 21)

    def test_negative_number_with_trailing_zero(self) -> None:
        self.assertEqual(self.solution.reverse(-120), -21)

    def test_largest_reversible_value_within_range(self) -> None:
        self.assertEqual(self.solution.reverse(1463847412), 2147483641)

    def test_smallest_reversible_value_within_range(self) -> None:
        self.assertEqual(self.solution.reverse(-1463847412), -2147483641)

    def test_negative_overflow_returns_zero(self) -> None:
        self.assertEqual(self.solution.reverse(-(2**31)), 0)


if __name__ == "__main__":
    unittest.main()
