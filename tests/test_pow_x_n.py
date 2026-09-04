"""Unit tests for Pow(x, n)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.pow_x_n import Solution


class TestPowXN(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.myPow(2.0, 5), 32.0)

    def test_second_worked_example(self) -> None:
        self.assertAlmostEqual(self.solution.myPow(1.1, 10), 2.59374, places=5)

    def test_third_worked_example(self) -> None:
        self.assertEqual(self.solution.myPow(2.0, -3), 0.125)

    def test_zero_exponent(self) -> None:
        self.assertEqual(self.solution.myPow(3.5, 0), 1)

    def test_negative_base_with_odd_exponent(self) -> None:
        self.assertEqual(self.solution.myPow(-2.0, 3), -8.0)

    def test_zero_with_positive_exponent(self) -> None:
        self.assertEqual(self.solution.myPow(0.0, 4), 0.0)


if __name__ == "__main__":
    unittest.main()
