"""Unit tests for Max Area of Island.

Test pseudocode:
    for each worked example:
        find the area of each connected group of land
        verify the largest area

    for edge cases taken directly from the rules:
        verify a single land cell has area one
        verify a single water cell has area zero
        verify diagonal land cells do not form a larger island
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.max_area_of_island import (
    Solution,
    example_grid_1,
    example_grid_2,
)


class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_largest_connected_island(self) -> None:
        self.assertEqual(self.solution.maxAreaOfIsland(example_grid_1()), 6)

    def test_grid_containing_only_water(self) -> None:
        self.assertEqual(self.solution.maxAreaOfIsland(example_grid_2()), 0)

    def test_single_land_cell(self) -> None:
        self.assertEqual(self.solution.maxAreaOfIsland([[1]]), 1)

    def test_single_water_cell(self) -> None:
        self.assertEqual(self.solution.maxAreaOfIsland([[0]]), 0)

    def test_diagonal_land_cells_are_separate(self) -> None:
        grid = [[1, 0], [0, 1]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)


if __name__ == "__main__":
    unittest.main()
