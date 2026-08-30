"""Unit tests for Coin Change II."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.coin_change_ii import Solution


class TestCoinChangeII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.change(4, [1, 2, 3]), 4)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.change(7, [2, 4]), 0)

    def test_zero_amount_has_one_empty_combination(self) -> None:
        self.assertEqual(self.solution.change(0, [1, 2, 3]), 1)

    def test_coin_order_does_not_duplicate_combinations(self) -> None:
        self.assertEqual(self.solution.change(4, [3, 2, 1]), 4)

    def test_single_coin_can_be_reused(self) -> None:
        self.assertEqual(self.solution.change(6, [2]), 1)

    def test_amount_below_every_coin_has_no_combination(self) -> None:
        self.assertEqual(self.solution.change(3, [4, 5]), 0)


if __name__ == "__main__":
    unittest.main()
