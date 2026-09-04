import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self) -> None:
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_one_day(self) -> None:
        self.assertEqual(self.solution.maxProfit([5]), 0)


if __name__ == "__main__":
    unittest.main()
