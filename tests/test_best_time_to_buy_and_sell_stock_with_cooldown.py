"""Unit tests for Best Time to Buy and Sell Stock with Cooldown."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.best_time_to_buy_and_sell_stock_with_cooldown import Solution


class TestBestTimeToBuyAndSellStockWithCooldown(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.maxProfit([1, 3, 4, 0, 4]), 6)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.maxProfit([1]), 0)

    def test_cooldown_prevents_buying_on_the_next_day(self) -> None:
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 0, 2]), 3)

    def test_prices_only_decrease(self) -> None:
        self.assertEqual(self.solution.maxProfit([5, 4, 3, 2, 1]), 0)

    def test_zero_price_coin_can_be_bought(self) -> None:
        self.assertEqual(self.solution.maxProfit([0, 4]), 4)

    def test_maximum_input_length(self) -> None:
        self.assertEqual(self.solution.maxProfit([1] * 5000), 0)


if __name__ == "__main__":
    unittest.main()
