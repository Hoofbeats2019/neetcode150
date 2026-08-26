"""Unit tests for Coin Change."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.coin_change import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.coinChange([1, 5, 10], 12), 3)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_third_worked_example(self) -> None:
        self.assertEqual(self.solution.coinChange([1], 0), 0)

    def test_exact_coin_needs_one_coin(self) -> None:
        self.assertEqual(self.solution.coinChange([7], 7), 1)

    def test_minimum_can_come_from_a_later_branch(self) -> None:
        self.assertEqual(self.solution.coinChange([1, 3, 4], 6), 2)

    def test_amount_below_every_coin_is_impossible(self) -> None:
        self.assertEqual(self.solution.coinChange([5, 7], 1), -1)

    def test_coin_order_does_not_change_the_result(self) -> None:
        self.assertEqual(self.solution.coinChange([10, 1, 5], 12), 3)

    def test_maximum_amount_with_unit_coin(self) -> None:
        self.assertEqual(self.solution.coinChange([1], 10_000), 10_000)


if __name__ == "__main__":
    unittest.main()
