"""Unit tests for Spiral Matrix."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.spiral_matrix import (
    Solution,
    example_matrix_1,
    example_matrix_2,
    example_matrix_3,
)


class TestSpiralMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.spiralOrder(example_matrix_1()), [1, 2, 4, 3])

    def test_second_worked_example(self) -> None:
        self.assertEqual(
            self.solution.spiralOrder(example_matrix_2()),
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        )

    def test_third_worked_example(self) -> None:
        self.assertEqual(
            self.solution.spiralOrder(example_matrix_3()),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        )

    def test_single_row(self) -> None:
        self.assertEqual(self.solution.spiralOrder([[1, 2, 3]]), [1, 2, 3])

    def test_single_column(self) -> None:
        self.assertEqual(self.solution.spiralOrder([[1], [2], [3]]), [1, 2, 3])

    def test_single_element(self) -> None:
        self.assertEqual(self.solution.spiralOrder([[42]]), [42])


if __name__ == "__main__":
    unittest.main()
