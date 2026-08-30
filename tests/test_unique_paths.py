"""Unit tests for Unique Paths."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.unique_paths import Solution


class TestUniquePaths(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.uniquePaths(3, 6), 21)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.uniquePaths(3, 3), 6)

    def test_single_cell_has_one_path(self) -> None:
        self.assertEqual(self.solution.uniquePaths(1, 1), 1)

    def test_single_row_has_one_path(self) -> None:
        self.assertEqual(self.solution.uniquePaths(1, 100), 1)

    def test_single_column_has_one_path(self) -> None:
        self.assertEqual(self.solution.uniquePaths(100, 1), 1)


if __name__ == "__main__":
    unittest.main()
