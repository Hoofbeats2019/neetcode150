"""Unit tests for Sum of Two Integers."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.sum_of_two_integers import Solution


class TestSumOfTwoIntegers(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.getSum(1, 1), 2)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.getSum(4, 7), 11)

    def test_zero_inputs(self) -> None:
        self.assertEqual(self.solution.getSum(0, 0), 0)

    def test_positive_and_negative_inputs(self) -> None:
        self.assertEqual(self.solution.getSum(-4, 7), 3)

    def test_two_negative_inputs(self) -> None:
        self.assertEqual(self.solution.getSum(-1000, -1000), -2000)


if __name__ == "__main__":
    unittest.main()
