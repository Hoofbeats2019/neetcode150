"""Unit tests for Burst Balloons."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.burst_balloons import Solution


class TestBurstBalloons(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_supplied_worked_example(self) -> None:
        self.assertEqual(self.solution.maxCoins([4, 2, 3, 7]), 143)

    def test_single_balloon_uses_virtual_boundaries(self) -> None:
        self.assertEqual(self.solution.maxCoins([7]), 7)

    def test_zero_value_balloon_can_be_burst_first(self) -> None:
        self.assertEqual(self.solution.maxCoins([0, 1]), 1)

    def test_all_zero_value_balloons(self) -> None:
        self.assertEqual(self.solution.maxCoins([0, 0, 0]), 0)

    def test_multiple_burst_orders(self) -> None:
        self.assertEqual(self.solution.maxCoins([3, 1, 5, 8]), 167)


if __name__ == "__main__":
    unittest.main()
