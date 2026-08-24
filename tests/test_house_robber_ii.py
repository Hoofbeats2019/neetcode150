"""Unit tests for House Robber II."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.house_robber_ii import Solution


class TestHouseRobberII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.rob([3, 4, 3]), 4)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.rob([2, 9, 8, 3, 6]), 15)

    def test_one_house(self) -> None:
        self.assertEqual(self.solution.rob([7]), 7)

    def test_two_houses(self) -> None:
        self.assertEqual(self.solution.rob([5, 9]), 9)

    def test_all_houses_have_no_money(self) -> None:
        self.assertEqual(self.solution.rob([0, 0, 0]), 0)

    def test_first_and_last_cannot_both_be_robbed(self) -> None:
        self.assertEqual(self.solution.rob([10, 1, 1, 10]), 11)


if __name__ == "__main__":
    unittest.main()
