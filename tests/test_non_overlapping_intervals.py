"""Unit tests for Non-Overlapping Intervals."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.non_overlapping_intervals import Solution


class TestNonOverlappingIntervals(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(
            self.solution.eraseOverlapIntervals([[1, 2], [2, 4], [1, 4]]), 1
        )

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.eraseOverlapIntervals([[1, 2], [2, 4]]), 0)

    def test_contained_intervals_keep_the_earliest_end(self) -> None:
        self.assertEqual(
            self.solution.eraseOverlapIntervals([[1, 100], [11, 12], [12, 13]]),
            1,
        )

    def test_all_overlapping_intervals(self) -> None:
        self.assertEqual(
            self.solution.eraseOverlapIntervals([[1, 4], [2, 3], [3, 5]]), 1
        )

    def test_single_interval(self) -> None:
        self.assertEqual(self.solution.eraseOverlapIntervals([[4, 5]]), 0)


if __name__ == "__main__":
    unittest.main()
