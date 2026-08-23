"""Unit tests for Swim in Rising Water."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.swim_in_rising_water import (
    Solution,
    example_grid_1,
    example_grid_2,
)


class TestSwimInRisingWater(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(
            self.solution.swimInWater(example_grid_1()),
            3,
        )

    def test_second_worked_example(self) -> None:
        self.assertEqual(
            self.solution.swimInWater(example_grid_2()),
            8,
        )

    def test_single_cell_uses_its_own_elevation(self) -> None:
        self.assertEqual(self.solution.swimInWater([[0]]), 0)

    def test_starting_elevation_can_determine_the_answer(self) -> None:
        grid = [[3, 2], [0, 1]]
        self.assertEqual(self.solution.swimInWater(grid), 3)

    def test_path_cost_is_its_highest_elevation(self) -> None:
        grid = [
            [0, 8, 7],
            [1, 2, 6],
            [5, 3, 4],
        ]
        self.assertEqual(self.solution.swimInWater(grid), 4)


if __name__ == "__main__":
    unittest.main()
