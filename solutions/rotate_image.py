"""Rotate Image.

Created: 3 September 2026
Created by: Yanlong Su

Given a square ``n x n`` matrix of integers ``matrix``, rotate it by 90
degrees clockwise.

Rotate the matrix in place. Do not allocate another 2-D matrix, and do not
return anything.

Example 1:
    Input: matrix = [[1, 2], [3, 4]]
    Output: [[3, 1], [4, 2]]

Example 2:
    Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Constraints:
    n == len(matrix) == len(matrix[row])
    1 <= n <= 20
    -1000 <= matrix[row][column] <= 1000

Pseudocode:
    rotate(matrix):
        reverse the order of the rows

        for each cell strictly above the main diagonal:
            swap it with its reflected cell across the diagonal

Time complexity: O(n^2)
Space complexity: O(1)
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """Rotate matrix 90 degrees clockwise in place."""
        matrix.reverse()

        for row in range(len(matrix)):
            for column in range(row + 1, len(matrix)):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column],
                )


def example_matrix_1() -> list[list[int]]:
    """Return a fresh copy of the first worked example matrix."""
    return [[1, 2], [3, 4]]


def example_matrix_2() -> list[list[int]]:
    """Return a fresh copy of the second worked example matrix."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_example_1() -> None:
    """Run the first worked example."""
    matrix = example_matrix_1()
    result = Solution().rotate(matrix)
    assert result is None
    assert matrix == [[3, 1], [4, 2]]


def test_example_2() -> None:
    """Run the second worked example."""
    matrix = example_matrix_2()
    result = Solution().rotate(matrix)
    assert result is None
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
