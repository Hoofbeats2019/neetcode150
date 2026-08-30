"""Unique Paths.

Created: 30 August 2026
Created by: Yanlong Su

There is an ``m x n`` grid. Starting at the top-left cell ``(0, 0)``, you
may move only one cell right or one cell down at a time.

Return the number of unique paths that reach the bottom-right cell
``(m - 1, n - 1)``. The result fits in a 32-bit integer.

Example 1:
    Input: m = 3, n = 6
    Output: 21

Example 2:
    Input: m = 3, n = 3
    Output: 6

Constraints:
    1 <= m, n <= 100

Pseudocode:
    uniquePaths(m, n, row = 0, col = 0, memo = null):
        create an m by n memo grid filled with -1 on the first call
        if the current cell is the bottom-right cell, return 1
        if this cell has a memoized result, return it

        paths = 0
        if moving right remains in the grid, add the recursive result
        if moving down remains in the grid, add the recursive result

        store and return paths for the current cell

Time complexity: O(m * n)
Space complexity: O(m * n)
"""


class Solution:
    def uniquePaths(
        self,
        m: int,
        n: int,
        row: int = 0,
        col: int = 0,
        memo: list[list[int]] | None = None,
    ) -> int:
        """Return the number of right-and-down paths from ``(row, col)``."""
        if memo is None:
            memo = [[-1] * n for _ in range(m)]

        if row == m - 1 and col == n - 1:
            return 1

        if memo[row][col] != -1:
            return memo[row][col]

        paths = 0

        if col + 1 < n:
            paths += self.uniquePaths(m, n, row, col + 1, memo)

        if row + 1 < m:
            paths += self.uniquePaths(m, n, row + 1, col, memo)

        memo[row][col] = paths
        return paths


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().uniquePaths(3, 6) == 21


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().uniquePaths(3, 3) == 6


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
