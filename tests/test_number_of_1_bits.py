"""Unit tests for Number of 1 Bits."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.number_of_1_bits import Solution


class TestNumberOf1Bits(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.hammingWeight(23), 4)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.hammingWeight(2147483645), 30)

    def test_zero_has_no_set_bits(self) -> None:
        self.assertEqual(self.solution.hammingWeight(0), 0)

    def test_largest_allowed_input_has_thirty_one_set_bits(self) -> None:
        self.assertEqual(self.solution.hammingWeight(2**31 - 1), 31)


if __name__ == "__main__":
    unittest.main()
