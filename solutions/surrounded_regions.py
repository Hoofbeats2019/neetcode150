"""Surrounded Regions.

Created: 22 August 2026
Created by: Yanlong Su

You are given an ``m x n`` matrix ``board`` containing ``"X"`` and ``"O"``.
Cells are connected horizontally or vertically, and connected ``"O"`` cells
form a region.

A region is surrounded when none of its ``"O"`` cells touch an edge of the
board. Capture every surrounded region by replacing all of its ``"O"`` cells
with ``"X"`` cells in place. Do not return anything.

Example 1:
    Input:
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    Output:
        [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]

    Explanation: The bottom ``"O"`` is not captured because it touches the
    edge of the board.

Example 2:
    Input:
        board = [["X"]]
    Output:
        [["X"]]

Constraints:
    1 <= len(board), len(board[i]) <= 200
    ``board[i][j]`` is ``"X"`` or ``"O"``.

Pseudocode:
    solve(board):
        create an empty visited set

        for each position in the board:
            if the position contains "O" and has not been visited:
                create an empty component list
                set touches edge to false
                add the position to a DFS stack

                while the stack is not empty:
                    remove the last position from the stack
                    skip it if it has already been visited
                    add it to visited and to the current component

                    if the position is on an edge:
                        set touches edge to true

                    for each top, bottom, left, and right neighbor:
                        if the neighbor is inside the board, contains "O",
                        and has not been visited:
                            add it to the stack

                if the component does not touch an edge:
                    change every position in the component from "O" to "X"

Time complexity: O(rows * columns)
Space complexity: O(rows * columns)
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Capture surrounded regions by modifying board in place."""
        visited: set[tuple[int, int]] = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        for start_row in range(len(board)):
            for start_column in range(len(board[start_row])):
                start = (start_row, start_column)

                if board[start_row][start_column] != "O" or start in visited:
                    continue

                component: list[tuple[int, int]] = []
                touches_edge = False
                stack = [start]

                while stack:
                    row, column = stack.pop()

                    if (row, column) in visited:
                        continue

                    visited.add((row, column))
                    component.append((row, column))

                    if (
                        row == 0
                        or row == len(board) - 1
                        or column == 0
                        or column == len(board[row]) - 1
                    ):
                        touches_edge = True

                    for row_change, column_change in directions:
                        neighbor_row = row + row_change
                        neighbor_column = column + column_change

                        if not 0 <= neighbor_row < len(board):
                            continue

                        if not 0 <= neighbor_column < len(board[neighbor_row]):
                            continue

                        neighbor = (neighbor_row, neighbor_column)

                        if (
                            board[neighbor_row][neighbor_column] == "O"
                            and neighbor not in visited
                        ):
                            stack.append(neighbor)

                if not touches_edge:
                    for row, column in component:
                        board[row][column] = "X"


def example_board_1() -> list[list[str]]:
    """Return a fresh copy of the first example board."""
    return [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]


def example_board_2() -> list[list[str]]:
    """Return a fresh copy of the second example board."""
    return [["X"]]


def test_example_1() -> None:
    """Run the first worked example."""
    board = example_board_1()
    result = Solution().solve(board)
    assert result is None
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]


def test_example_2() -> None:
    """Run the second worked example."""
    board = example_board_2()
    result = Solution().solve(board)
    assert result is None
    assert board == [["X"]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
