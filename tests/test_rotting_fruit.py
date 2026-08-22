"""Unit tests for Rotting Fruit.

Test pseudocode:
    for each worked example:
        verify the expected minimum time or impossible result

    for edge cases taken directly from the rules:
        verify a grid with no fresh fruit needs zero minutes
        verify a fresh fruit adjacent to rotten fruit needs one minute
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.rotting_fruit import (
    Solution,
    example_grid_1,
    example_grid_2,
)


class TestRottingFruit(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_all_fresh_fruit_eventually_rots(self) -> None:
        self.assertEqual(self.solution.orangesRotting(example_grid_1()), 4)

    def test_isolated_fresh_fruit_cannot_rot(self) -> None:
        self.assertEqual(self.solution.orangesRotting(example_grid_2()), -1)

    def test_no_fresh_fruit_needs_zero_minutes(self) -> None:
        self.assertEqual(self.solution.orangesRotting([[0, 2]]), 0)

    def test_adjacent_fresh_fruit_needs_one_minute(self) -> None:
        self.assertEqual(self.solution.orangesRotting([[2, 1]]), 1)

    def test_grid_with_only_fresh_fruit_is_impossible(self) -> None:
        self.assertEqual(self.solution.orangesRotting([[1, 1]]), -1)


if __name__ == "__main__":
    unittest.main()
