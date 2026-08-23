"""Unit tests for Climbing Stairs."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_one_step_has_one_way(self) -> None:
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_four_steps_has_five_ways(self) -> None:
        self.assertEqual(self.solution.climbStairs(4), 5)

    def test_maximum_input(self) -> None:
        self.assertEqual(self.solution.climbStairs(45), 1_836_311_903)


if __name__ == "__main__":
    unittest.main()
