"""Unit tests for Rotate Image."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.rotate_image import Solution, example_matrix_1, example_matrix_2


class TestRotateImage(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        matrix = example_matrix_1()
        result = self.solution.rotate(matrix)
        self.assertIsNone(result)
        self.assertEqual(matrix, [[3, 1], [4, 2]])

    def test_second_worked_example(self) -> None:
        matrix = example_matrix_2()
        self.solution.rotate(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_single_cell_matrix_is_unchanged(self) -> None:
        matrix = [[42]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, [[42]])

    def test_four_by_four_matrix(self) -> None:
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16],
        ]
        self.solution.rotate(matrix)
        self.assertEqual(
            matrix,
            [
                [15, 13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7, 10, 11],
            ],
        )


if __name__ == "__main__":
    unittest.main()
