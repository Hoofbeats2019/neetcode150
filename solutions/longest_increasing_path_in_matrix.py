"""Longest Increasing Path in Matrix.

Created: 31 August 2026
Created by: Yanlong Su

You are given a 2-D grid of non-negative integers ``matrix``. Return the
length of the longest strictly increasing path within ``matrix``.

From a cell in the path, you may move horizontally or vertically to an
adjacent cell. Diagonal moves are not allowed.

Example 1:
    Input: matrix = [[5, 5, 3], [2, 3, 6], [1, 1, 1]]
    Output: 4
    Explanation: One longest path is [1, 2, 3, 6].

Example 2:
    Input: matrix = [[1, 2, 3], [2, 1, 4], [7, 6, 5]]
    Output: 7
    Explanation: The longest path is [1, 2, 3, 4, 5, 6, 7].

Constraints:
    1 <= len(matrix), len(matrix[row]) <= 100
    0 <= matrix[row][column]

Pseudocode:
    longestIncreasingPath(matrix):
        create a memo grid initialized to 0
        for each cell, find the longest path beginning at that cell with DFS
        return the largest path length found

    dfs(row, column):
        return the cached result when this cell has already been calculated
        start the best path length at 1
        for each horizontal or vertical neighbor with a greater value:
            extend the path by calling DFS on that neighbor
        cache and return the best path length

Time complexity: O(rows * columns)
Space complexity: O(rows * columns)
"""

import sys


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """Return the length of the longest strictly increasing path."""
        rows = len(matrix)
        columns = len(matrix[0])
        required_limit = rows * columns + 100

        if sys.getrecursionlimit() < required_limit:
            sys.setrecursionlimit(required_limit)

        memo = [[0] * columns for _ in range(rows)]
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row: int, column: int) -> int:
            """Return the longest increasing path beginning at one cell."""
            if memo[row][column] != 0:
                return memo[row][column]

            best_path = 1

            for row_change, column_change in directions:
                neighbor_row = row + row_change
                neighbor_column = column + column_change

                if not 0 <= neighbor_row < rows:
                    continue

                if not 0 <= neighbor_column < columns:
                    continue

                if matrix[neighbor_row][neighbor_column] <= matrix[row][column]:
                    continue

                best_path = max(
                    best_path,
                    1 + dfs(neighbor_row, neighbor_column),
                )

            memo[row][column] = best_path
            return best_path

        longest_path = 0

        for row in range(rows):
            for column in range(columns):
                longest_path = max(longest_path, dfs(row, column))

        return longest_path


def example_matrix_1() -> list[list[int]]:
    """Return a fresh copy of the first worked example matrix."""
    return [[5, 5, 3], [2, 3, 6], [1, 1, 1]]


def example_matrix_2() -> list[list[int]]:
    """Return a fresh copy of the second worked example matrix."""
    return [[1, 2, 3], [2, 1, 4], [7, 6, 5]]


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().longestIncreasingPath(example_matrix_1()) == 4


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().longestIncreasingPath(example_matrix_2()) == 7


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
