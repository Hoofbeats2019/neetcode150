"""Spiral Matrix.

Created: 3 September 2026
Created by: Yanlong Su

Given an ``m x n`` matrix of integers ``matrix``, return a list containing
every element of ``matrix`` in spiral order.

Example 1:
    Input: matrix = [[1, 2], [3, 4]]
    Output: [1, 2, 4, 3]

Example 2:
    Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 3:
    Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Constraints:
    1 <= len(matrix), len(matrix[row]) <= 10
    -100 <= matrix[row][column] <= 100

Pseudocode:
    spiralOrder(matrix):
        set top, bottom, left, and right to the matrix boundaries

        while the remaining boundaries form a non-empty rectangle:
            traverse the top row from left to right, then move top down
            traverse the right column from top to bottom, then move right left
            if a row remains, traverse the bottom row right to left, then move bottom up
            if a column remains, traverse the left column bottom to top, then move left right

Time complexity: O(rows * columns)
Space complexity: O(1) auxiliary space
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """Return the matrix elements in clockwise spiral order."""
        result: list[int] = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for column in range(left, right + 1):
                result.append(matrix[top][column])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for column in range(right, left - 1, -1):
                    result.append(matrix[bottom][column])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result


def example_matrix_1() -> list[list[int]]:
    """Return a fresh copy of the first worked example matrix."""
    return [[1, 2], [3, 4]]


def example_matrix_2() -> list[list[int]]:
    """Return a fresh copy of the second worked example matrix."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def example_matrix_3() -> list[list[int]]:
    """Return a fresh copy of the third worked example matrix."""
    return [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().spiralOrder(example_matrix_1()) == [1, 2, 4, 3]


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().spiralOrder(example_matrix_2()) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_example_3() -> None:
    """Run the third worked example."""
    assert Solution().spiralOrder(example_matrix_3()) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
