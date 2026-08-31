"""Unit tests for Longest Increasing Path in Matrix."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.longest_increasing_path_in_matrix import (
    Solution,
    example_matrix_1,
    example_matrix_2,
)


class TestLongestIncreasingPathInMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.longestIncreasingPath(example_matrix_1()), 4)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.longestIncreasingPath(example_matrix_2()), 7)

    def test_single_cell_path_has_length_one(self) -> None:
        self.assertEqual(self.solution.longestIncreasingPath([[0]]), 1)

    def test_equal_adjacent_values_cannot_extend_a_path(self) -> None:
        self.assertEqual(self.solution.longestIncreasingPath([[2, 2]]), 1)

    def test_path_cannot_move_diagonally(self) -> None:
        self.assertEqual(self.solution.longestIncreasingPath([[1, 0], [0, 2]]), 2)

    def test_single_column_increasing_path(self) -> None:
        self.assertEqual(
            self.solution.longestIncreasingPath([[1], [2], [3], [4]]),
            4,
        )


if __name__ == "__main__":
    unittest.main()
