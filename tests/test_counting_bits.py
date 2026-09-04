"""Unit tests for Counting Bits."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.counting_bits import Solution


class TestCountingBits(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_worked_example(self) -> None:
        self.assertEqual(self.solution.countBits(4), [0, 1, 1, 2, 1])

    def test_zero(self) -> None:
        self.assertEqual(self.solution.countBits(0), [0])

    def test_odd_numbers_add_one_to_their_halves(self) -> None:
        self.assertEqual(self.solution.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_largest_allowed_input(self) -> None:
        counts = self.solution.countBits(1000)

        self.assertEqual(len(counts), 1001)
        self.assertEqual(counts[1000], 6)


if __name__ == "__main__":
    unittest.main()
