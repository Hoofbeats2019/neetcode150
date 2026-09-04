"""Valid Sudoku.

Return whether a partially filled 9-by-9 Sudoku board has no repeated digit in
any row, column, or 3-by-3 box.
"""

from collections import defaultdict
from typing import DefaultDict, List, Set


class Solution:
    """Track each row, column, and box's already-seen digits."""

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: DefaultDict[int, Set[str]] = defaultdict(set)
        columns: DefaultDict[int, Set[str]] = defaultdict(set)
        boxes: DefaultDict[tuple[int, int], Set[str]] = defaultdict(set)

        for row in range(9):
            for column in range(9):
                digit = board[row][column]
                if digit == ".":
                    continue
                box = (row // 3, column // 3)
                if digit in rows[row] or digit in columns[column] or digit in boxes[box]:
                    return False
                rows[row].add(digit)
                columns[column].add(digit)
                boxes[box].add(digit)
        return True


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert Solution().isValidSudoku(board)
    print("The worked example passed.")
