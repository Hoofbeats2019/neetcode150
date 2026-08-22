"""N-Queens.

Created: 22 August 2026
Created by: Yanlong Su

Place ``n`` queens on an ``n x n`` chessboard so that no two queens can
attack each other. A queen can attack horizontally, vertically, and
diagonally.

Return every distinct valid board layout in any order. In each board string,
``"Q"`` represents a queen and ``"."`` represents an empty space.

Example 1:
    Input: n = 4
    Output: [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    Explanation: There are two distinct solutions to the 4-queens puzzle.

Example 2:
    Input: n = 1
    Output: [["Q"]]

Constraints:
    1 <= n <= 8

Pseudocode:
    solveNQueens(n):
        create an empty result list
        create an n x n board filled with empty spaces
        create sets for occupied columns and both diagonal directions

        backtrack(row):
            if row equals n:
                convert the board rows to strings
                add a copy of the board layout to result
                return

            for each column in the current row:
                calculate both diagonal identifiers

                if the column or either diagonal is occupied:
                    continue

                place a queen and mark its column and diagonals
                backtrack(row + 1)
                remove the queen and unmark its column and diagonals

        backtrack(0)
        return result

Time complexity: O(n! + S * n^2), where S is the number of solutions
Space complexity: O(n^2) auxiliary; O(S * n^2) for returned boards
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """Return every distinct valid arrangement of n queens."""
        result: list[list[str]] = []
        board = [["."] * n for _ in range(n)]

        occupied_columns: set[int] = set()
        occupied_positive_diagonals: set[int] = set()
        occupied_negative_diagonals: set[int] = set()

        def backtrack(row: int) -> None:
            """Place one queen in row, then explore the next row."""
            # A path reaching beyond the last row is a complete solution.
            if row == n:
                result.append(["".join(board_row) for board_row in board])
                return

            # Every column in this row represents one possible child node.
            for column in range(n):
                positive_diagonal = row + column
                negative_diagonal = row - column

                # PRUNE a placement attacked by an existing queen.
                if (
                    column in occupied_columns
                    or positive_diagonal in occupied_positive_diagonals
                    or negative_diagonal in occupied_negative_diagonals
                ):
                    continue

                # MAKE THE CHOICE.
                board[row][column] = "Q"
                occupied_columns.add(column)
                occupied_positive_diagonals.add(positive_diagonal)
                occupied_negative_diagonals.add(negative_diagonal)

                # EXPLORE the next layer of the search graph.
                backtrack(row + 1)

                # UNDO THE CHOICE before trying another column.
                board[row][column] = "."
                occupied_columns.remove(column)
                occupied_positive_diagonals.remove(positive_diagonal)
                occupied_negative_diagonals.remove(negative_diagonal)

        # This call represents the conceptual initial node above the board.
        backtrack(0)
        return result


def normalize(boards: list[list[str]]) -> list[tuple[str, ...]]:
    """Normalize solution ordering for the executable examples."""
    return sorted(tuple(board) for board in boards)


def test_example_1() -> None:
    actual = Solution().solveNQueens(4)
    expected = [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().solveNQueens(1)
    assert actual == [["Q"]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
