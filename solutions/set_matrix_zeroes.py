"""Set Matrix Zeroes.

Created: 4 September 2026
Created by: Yanlong Su

Given an ``m x n`` integer matrix ``matrix``, if an element is ``0``, set its
entire row and column to ``0``. Modify the matrix in place and do not return
anything.

Example 1:
    Input: matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

Example 2:
    Input: matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

Constraints:
    1 <= len(matrix), len(matrix[row]) <= 200
    -2^31 <= matrix[row][column] <= 2^31 - 1

Pseudocode:
    setZeroes(matrix):
        record whether the original first row contains a zero
        record whether the original first column contains a zero

        for each inner cell:
            if the cell is zero:
                set its first-column row marker to zero
                set its first-row column marker to zero

        for each inner cell:
            if its row marker or column marker is zero:
                set the cell to zero

        if the original first row had a zero:
            set every first-row cell to zero

        if the original first column had a zero:
            set every first-column cell to zero

Time complexity: O(rows * columns)
Space complexity: O(1)
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Set every row and column containing a zero to zero in place."""
        rows = len(matrix)
        columns = len(matrix[0])
        first_row_has_zero = any(matrix[0][column] == 0 for column in range(columns))
        first_column_has_zero = any(matrix[row][0] == 0 for row in range(rows))

        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0

        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0

        if first_row_has_zero:
            for column in range(columns):
                matrix[0][column] = 0

        if first_column_has_zero:
            for row in range(rows):
                matrix[row][0] = 0


def example_matrix_1() -> list[list[int]]:
    """Return a fresh copy of the first worked example matrix."""
    return [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def example_matrix_2() -> list[list[int]]:
    """Return a fresh copy of the second worked example matrix."""
    return [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


def test_example_1() -> None:
    """Run the first worked example."""
    matrix = example_matrix_1()
    result = Solution().setZeroes(matrix)
    assert result is None
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_example_2() -> None:
    """Run the second worked example."""
    matrix = example_matrix_2()
    result = Solution().setZeroes(matrix)
    assert result is None
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
