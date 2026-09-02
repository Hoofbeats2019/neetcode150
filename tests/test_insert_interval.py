"""Unit tests for Insert Interval."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.insert_interval import Solution


class TestInsertInterval(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.insert([[1, 3], [4, 6]], [2, 5]), [[1, 6]])

    def test_second_worked_example(self) -> None:
        self.assertEqual(
            self.solution.insert([[1, 2], [3, 5], [9, 10]], [6, 7]),
            [[1, 2], [3, 5], [6, 7], [9, 10]],
        )

    def test_empty_intervals(self) -> None:
        self.assertEqual(self.solution.insert([], [2, 5]), [[2, 5]])

    def test_touching_intervals_are_merged(self) -> None:
        self.assertEqual(self.solution.insert([[1, 2], [5, 7]], [2, 5]), [[1, 7]])

    def test_merges_multiple_intervals(self) -> None:
        self.assertEqual(
            self.solution.insert([[1, 2], [3, 4], [5, 6], [8, 9]], [2, 8]),
            [[1, 9]],
        )


if __name__ == "__main__":
    unittest.main()
