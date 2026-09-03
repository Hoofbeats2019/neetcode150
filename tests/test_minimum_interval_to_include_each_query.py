"""Unit tests for Minimum Interval to Include Each Query."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.minimum_interval_to_include_each_query import Solution


class TestMinimumIntervalToIncludeEachQuery(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_worked_example(self) -> None:
        self.assertEqual(
            self.solution.minInterval(
                [[1, 3], [2, 3], [3, 7], [6, 6]], [2, 3, 1, 7, 6, 8]
            ),
            [2, 2, 3, 5, 1, -1],
        )

    def test_preserves_the_original_query_order(self) -> None:
        self.assertEqual(
            self.solution.minInterval([[2, 5], [1, 10]], [8, 3, 1, 6]),
            [10, 4, 10, 10],
        )

    def test_removes_intervals_that_have_ended(self) -> None:
        self.assertEqual(
            self.solution.minInterval([[1, 2], [5, 8]], [1, 3, 5, 8, 9]),
            [2, -1, 4, 4, -1],
        )

    def test_single_point_interval_is_shortest(self) -> None:
        self.assertEqual(
            self.solution.minInterval([[1, 10], [4, 4], [3, 6]], [4]), [1]
        )


if __name__ == "__main__":
    unittest.main()
