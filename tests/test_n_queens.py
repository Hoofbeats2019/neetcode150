"""Unit tests for N-Queens.

Test pseudocode:
    for each worked example:
        request every valid board layout
        normalize the result ordering
        verify the expected layouts are returned exactly once

    for direct edge cases:
        verify board sizes with no valid arrangement return an empty list
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.n_queens import Solution


class TestNQueens(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertBoardsEqual(
        self,
        actual: list[list[str]],
        expected: list[list[str]],
    ) -> None:
        normalized_actual = sorted(tuple(board) for board in actual)
        normalized_expected = sorted(tuple(board) for board in expected)
        self.assertEqual(normalized_actual, normalized_expected)

    def test_four_queens(self) -> None:
        actual = self.solution.solveNQueens(4)
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]
        self.assertBoardsEqual(actual, expected)

    def test_one_queen(self) -> None:
        self.assertEqual(self.solution.solveNQueens(1), [["Q"]])

    def test_two_queens_has_no_solution(self) -> None:
        self.assertEqual(self.solution.solveNQueens(2), [])

    def test_three_queens_has_no_solution(self) -> None:
        self.assertEqual(self.solution.solveNQueens(3), [])


if __name__ == "__main__":
    unittest.main()
