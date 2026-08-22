"""Unit tests for Number of Islands.

Test pseudocode:
    for each worked example:
        count the separate groups of connected land
        verify the expected island count

    for edge cases taken directly from the rules:
        verify a single land cell is one island
        verify a single water cell has no islands
        verify diagonally adjacent land cells are separate islands
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.number_of_islands import (
    Solution,
    example_grid_1,
    example_grid_2,
)


class TestNumberOfIslands(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_connected_island(self) -> None:
        self.assertEqual(self.solution.numIslands(example_grid_1()), 1)

    def test_four_separate_islands(self) -> None:
        self.assertEqual(self.solution.numIslands(example_grid_2()), 4)

    def test_single_land_cell(self) -> None:
        self.assertEqual(self.solution.numIslands([["1"]]), 1)

    def test_single_water_cell(self) -> None:
        self.assertEqual(self.solution.numIslands([["0"]]), 0)

    def test_diagonal_land_cells_are_separate(self) -> None:
        grid = [["1", "0"], ["0", "1"]]
        self.assertEqual(self.solution.numIslands(grid), 2)


if __name__ == "__main__":
    unittest.main()
