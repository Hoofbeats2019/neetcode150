"""Unit tests for House Robber."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.house_robber import Solution


class TestHouseRobber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.rob([1, 1, 3, 3]), 4)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.rob([2, 9, 8, 3, 6]), 16)

    def test_one_house(self) -> None:
        self.assertEqual(self.solution.rob([7]), 7)

    def test_two_houses(self) -> None:
        self.assertEqual(self.solution.rob([5, 9]), 9)

    def test_all_houses_have_no_money(self) -> None:
        self.assertEqual(self.solution.rob([0, 0, 0]), 0)

    def test_skipping_two_adjacent_high_value_houses(self) -> None:
        self.assertEqual(self.solution.rob([4, 10, 3, 1, 5]), 15)


if __name__ == "__main__":
    unittest.main()
