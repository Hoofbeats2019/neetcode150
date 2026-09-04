"""Unit tests for Detect Squares."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.detect_squares import CountSquares


class TestDetectSquares(unittest.TestCase):
    def test_worked_example(self) -> None:
        count_squares = CountSquares()
        count_squares.add([1, 1])
        count_squares.add([2, 2])
        count_squares.add([1, 2])

        self.assertEqual(count_squares.count([2, 1]), 1)
        self.assertEqual(count_squares.count([3, 3]), 0)

        count_squares.add([2, 2])
        self.assertEqual(count_squares.count([2, 1]), 2)

    def test_squares_on_both_sides_of_the_query_point(self) -> None:
        count_squares = CountSquares()
        for point in ([1, 0], [0, 0], [0, 1], [2, 0], [2, 1]):
            count_squares.add(point)

        self.assertEqual(count_squares.count([1, 1]), 2)

    def test_missing_corner_prevents_a_square(self) -> None:
        count_squares = CountSquares()
        for point in ([0, 0], [0, 2]):
            count_squares.add(point)

        self.assertEqual(count_squares.count([2, 0]), 0)

    def test_duplicate_points_multiply_the_number_of_choices(self) -> None:
        count_squares = CountSquares()
        for point in ([0, 0], [0, 0], [0, 1], [1, 0], [1, 1]):
            count_squares.add(point)

        self.assertEqual(count_squares.count([1, 0]), 2)


if __name__ == "__main__":
    unittest.main()
