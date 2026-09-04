"""Unit tests for Reverse Bits."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.reverse_bits import Solution


class TestReverseBits(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.reverseBits(21), 2818572288)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.reverseBits(43261596), 964176192)

    def test_zero_remains_zero(self) -> None:
        self.assertEqual(self.solution.reverseBits(0), 0)

    def test_all_bits_set_remains_unchanged(self) -> None:
        self.assertEqual(self.solution.reverseBits(2**32 - 1), 2**32 - 1)

    def test_lowest_bit_moves_to_highest_position(self) -> None:
        self.assertEqual(self.solution.reverseBits(1), 2**31)


if __name__ == "__main__":
    unittest.main()
