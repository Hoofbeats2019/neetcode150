"""Unit tests for K Closest Points to Origin.

Test pseudocode:
    for each worked example:
        request the k closest points
        verify the expected points are returned in any order

    for edge cases:
        verify a single point is returned
        verify all points are returned when k equals the number of points

"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.k_closest_points_to_origin import Solution


class TestKClosestPointsToOrigin(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertPointsEqual(
        self, actual: list[list[int]], expected: list[list[int]]
    ) -> None:
        self.assertEqual(sorted(actual), sorted(expected))

    def test_first_example(self) -> None:
        actual = self.solution.kClosest([[0, 2], [2, 2]], 1)
        self.assertPointsEqual(actual, [[0, 2]])

    def test_second_example(self) -> None:
        actual = self.solution.kClosest([[0, 2], [2, 0], [2, 2]], 2)
        self.assertPointsEqual(actual, [[0, 2], [2, 0]])

    def test_single_point(self) -> None:
        actual = self.solution.kClosest([[-3, 4]], 1)
        self.assertPointsEqual(actual, [[-3, 4]])

    def test_k_equals_number_of_points(self) -> None:
        points = [[1, 1], [-1, -1], [3, 4]]
        actual = self.solution.kClosest(points, len(points))
        self.assertPointsEqual(actual, points)


if __name__ == "__main__":
    unittest.main()
