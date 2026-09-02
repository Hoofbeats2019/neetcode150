"""Unit tests for Jump Game II."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.jump_game_ii import Solution


class TestJumpGameII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.jump([2, 4, 1, 1, 1, 1]), 2)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.jump([2, 1, 2, 1, 0]), 2)

    def test_single_index_needs_no_jumps(self) -> None:
        self.assertEqual(self.solution.jump([0]), 0)

    def test_best_first_jump_is_not_the_farthest_index(self) -> None:
        self.assertEqual(self.solution.jump([2, 3, 1, 1, 4]), 2)


if __name__ == "__main__":
    unittest.main()
