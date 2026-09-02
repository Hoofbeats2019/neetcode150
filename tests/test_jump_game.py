"""Unit-test scaffold for Jump Game."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.jump_game import Solution


class TestJumpGame(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(self.solution.canJump([1, 2, 0, 1, 0]))

    def test_second_worked_example(self) -> None:
        self.assertFalse(self.solution.canJump([1, 2, 1, 0, 1]))

    def test_single_index_is_reachable(self) -> None:
        self.assertTrue(self.solution.canJump([0]))

    def test_zero_before_the_final_index_blocks_progress(self) -> None:
        self.assertFalse(self.solution.canJump([1, 0, 1]))


if __name__ == "__main__":
    unittest.main()
