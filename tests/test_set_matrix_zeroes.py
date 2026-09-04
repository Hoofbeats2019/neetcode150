"""Unit tests for Set Matrix Zeroes.

Test pseudocode:
    for each worked example:
        set affected rows and columns to zero in place
        verify the method returns nothing

    for edge cases taken directly from the rules:
        zero the first row when it originally contains a zero
        zero the first column when it originally contains a zero
        leave a matrix without zeroes unchanged
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.set_matrix_zeroes import Solution, example_matrix_1, example_matrix_2


class TestSetMatrixZeroes(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        matrix = example_matrix_1()
        result = self.solution.setZeroes(matrix)
        self.assertIsNone(result)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_second_worked_example(self) -> None:
        matrix = example_matrix_2()
        result = self.solution.setZeroes(matrix)
        self.assertIsNone(result)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_zero_in_first_row(self) -> None:
        matrix = [[1, 0, 3], [4, 5, 6], [7, 8, 9]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0], [4, 0, 6], [7, 0, 9]])

    def test_zero_in_first_column(self) -> None:
        matrix = [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0, 2, 3], [0, 0, 0], [0, 8, 9]])

    def test_matrix_without_zeroes_is_unchanged(self) -> None:
        matrix = [[1, 2], [3, 4]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1, 2], [3, 4]])


if __name__ == "__main__":
    unittest.main()
