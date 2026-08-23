"""Unit tests for Min Cost to Connect Points."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.min_cost_to_connect_points import Solution


class TestMinCostToConnectPoints(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_points_with_positive_coordinates(self) -> None:
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 20)

    def test_points_with_negative_coordinates(self) -> None:
        points = [[3, 12], [-2, 5], [-4, 1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 18)

    def test_single_point_has_zero_cost(self) -> None:
        self.assertEqual(self.solution.minCostConnectPoints([[4, -7]]), 0)

    def test_two_points_use_their_manhattan_distance(self) -> None:
        points = [[-1, -2], [3, 4]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 10)

    def test_cycle_forming_edge_is_skipped(self) -> None:
        points = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 3)


if __name__ == "__main__":
    unittest.main()
