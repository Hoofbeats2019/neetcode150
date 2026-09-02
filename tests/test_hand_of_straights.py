"""Unit tests for Hand of Straights."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.hand_of_straights import Solution


class TestHandOfStraights(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(
            self.solution.isNStraightHand([1, 2, 4, 2, 3, 5, 3, 4], 4)
        )

    def test_second_worked_example(self) -> None:
        self.assertFalse(
            self.solution.isNStraightHand([1, 2, 3, 3, 4, 5, 6, 7], 4)
        )

    def test_repeated_consecutive_groups(self) -> None:
        self.assertTrue(self.solution.isNStraightHand([1, 1, 2, 2, 3, 3], 3))

    def test_missing_required_card(self) -> None:
        self.assertFalse(self.solution.isNStraightHand([1, 2, 4, 5, 6, 7], 3))

    def test_hand_length_not_divisible_by_group_size(self) -> None:
        self.assertFalse(self.solution.isNStraightHand([1, 2, 3, 4, 5], 2))

    def test_group_size_one(self) -> None:
        self.assertTrue(self.solution.isNStraightHand([4, 2, 2, 9], 1))


if __name__ == "__main__":
    unittest.main()
