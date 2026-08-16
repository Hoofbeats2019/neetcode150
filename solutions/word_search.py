"""Word Search.

Created: 16 August 2026
Created by: Yanlong Su

Given a 2-D grid of characters ``board`` and a string ``word``, return ``True``
if the word is present in the grid. Otherwise, return ``False``.

The word must be formed by a path of horizontally or vertically neighboring
cells. The same cell may not be used more than once in one word.

Example 1:
    Input:
        board = [
            ["A", "B", "C", "D"],
            ["S", "A", "A", "T"],
            ["A", "C", "A", "E"],
        ]
        word = "CAT"
    Output: True

Example 2:
    Input:
        board = [
            ["A", "B", "C", "D"],
            ["S", "A", "A", "T"],
            ["A", "C", "A", "E"],
        ]
        word = "BAT"
    Output: False

Constraints:
    1 <= len(board), len(board[i]) <= 5
    1 <= len(word) <= 10
    ``board`` and ``word`` contain only lowercase and uppercase English letters.

Pseudocode:
    exist(board, word):
        create an empty visited set

        backtrack(row, column, current_state):
            if current_state equals word:
                return True

            if the position is outside the board or already visited:
                return False

            current_index = length of current_state
            chosen_letter = board[row][column]

            if chosen_letter does not equal word[current_index]:
                return False

            add the position to visited
            append chosen_letter to current_state

            for each horizontal or vertical neighboring position:
                if backtrack(neighbor row, neighbor column, current_state):
                    remove the position from visited
                    return True

            remove the position from visited
            return False

        for every position in the board:
            if backtrack(position row, position column, ""):
                return True

        return False

Time complexity: O(rows * columns * L * 4^L), where L is len(word)
Space complexity: O(L^2) for recursive string states; O(L) for visited cells
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Return whether word can be formed by a valid path in board."""
        row_count = len(board)
        column_count = len(board[0])
        visited: set[tuple[int, int]] = set()

        def backtrack(
            row: int,
            column: int,
            current_state: str,
        ) -> bool:
            """Explore paths continuing from one chosen board position."""
            # VALID RESULT CHECK:
            is_valid_result = current_state == word

            if is_valid_result:
                return True

            # PRUNE positions that cannot be chosen.
            is_outside_board = not (
                0 <= row < row_count and 0 <= column < column_count
            )
            if is_outside_board or (row, column) in visited:
                return False

            # PRUNE a letter that cannot continue the required word prefix.
            current_index = len(current_state)
            chosen_letter = board[row][column]
            if chosen_letter != word[current_index]:
                return False

            # MAKE THE CHOICE.
            visited.add((row, column))
            current_state += chosen_letter

            # EXPLORE every horizontal and vertical neighboring cell.
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for row_change, column_change in directions:
                if backtrack(
                    row + row_change,
                    column + column_change,
                    current_state,
                ):
                    visited.remove((row, column))
                    return True

            # UNDO THE CHOICE before another path uses this cell.
            visited.remove((row, column))
            return False

        # Every cell is a possible starting position for the word.
        for row in range(row_count):
            for column in range(column_count):
                if backtrack(row, column, ""):
                    return True

        return False


def example_board() -> list[list[str]]:
    """Return a fresh copy of the board shared by both examples."""
    return [
        ["A", "B", "C", "D"],
        ["S", "A", "A", "T"],
        ["A", "C", "A", "E"],
    ]


def test_example_1() -> None:
    assert Solution().exist(example_board(), "CAT") is True


def test_example_2() -> None:
    assert Solution().exist(example_board(), "BAT") is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
