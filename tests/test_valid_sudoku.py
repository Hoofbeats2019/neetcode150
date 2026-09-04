import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.valid_sudoku import Solution


class TestValidSudoku(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    def test_valid_board(self) -> None:
        self.assertTrue(self.solution.isValidSudoku(self.board))

    def test_duplicate_in_row(self) -> None:
        self.board[0][2] = "5"
        self.assertFalse(self.solution.isValidSudoku(self.board))

    def test_duplicate_in_box(self) -> None:
        self.board[1][1] = "9"
        self.assertFalse(self.solution.isValidSudoku(self.board))


if __name__ == "__main__":
    unittest.main()
