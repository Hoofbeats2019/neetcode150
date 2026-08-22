"""Unit tests for Islands and Treasure."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.islands_and_treasure import (
    INF,
    Solution,
    example_grid_1,
    example_grid_2,
)


class TestIslandsAndTreasure(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_grid_with_two_treasures(self) -> None:
        grid = example_grid_1()
        result = self.solution.islandsAndTreasure(grid)
        self.assertIsNone(result)
        self.assertEqual(
            grid,
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4],
            ],
        )

    def test_small_grid(self) -> None:
        grid = example_grid_2()
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, [[0, -1], [1, 2]])

    def test_unreachable_land_remains_unchanged(self) -> None:
        grid = [[0, -1, INF]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, [[0, -1, INF]])

    def test_grid_with_only_treasure_and_water_is_unchanged(self) -> None:
        grid = [[0, -1], [-1, 0]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, [[0, -1], [-1, 0]])


if __name__ == "__main__":
    unittest.main()
