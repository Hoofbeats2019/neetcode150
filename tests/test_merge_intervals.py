"""Unit tests for Merge Intervals."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.merge_intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(
            self.solution.merge([[1, 3], [1, 5], [6, 7]]), [[1, 5], [6, 7]]
        )

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.merge([[1, 2], [2, 3]]), [[1, 3]])

    def test_unsorted_intervals(self) -> None:
        self.assertEqual(
            self.solution.merge([[8, 10], [1, 3], [2, 6], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )

    def test_contained_interval(self) -> None:
        self.assertEqual(self.solution.merge([[1, 10], [2, 3]]), [[1, 10]])

    def test_single_interval(self) -> None:
        self.assertEqual(self.solution.merge([[4, 4]]), [[4, 4]])


if __name__ == "__main__":
    unittest.main()
