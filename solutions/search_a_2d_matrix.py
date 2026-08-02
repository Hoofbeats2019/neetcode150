"""Search a 2D Matrix.

Created: 2 August 2026
Created by: Yanlong Su

You are given an ``m x n`` integer matrix and an integer ``target``.

Each row is sorted in non-decreasing order, and the first integer of every row
is greater than the last integer of the previous row.

Return True if ``target`` exists within the matrix. Otherwise, return False.

Example 1:
    Input: matrix = [[1, 2, 4, 8], [10, 11, 12, 13],
                     [14, 20, 30, 40]], target = 10
    Output: True

Example 2:
    Input: matrix = [[1, 2, 4, 8], [10, 11, 12, 13],
                     [14, 20, 30, 40]], target = 15
    Output: False

Executable examples:
    >>> solution = Solution()
    >>> matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    >>> solution.searchMatrix(matrix, 10)
    True
    >>> solution.searchMatrix(matrix, 15)
    False

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10000 <= matrix[i][j], target <= 10000
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_up = 0
        row_down = len(matrix) - 1
        column_left = 0
        column_right = len(matrix[0]) - 1

        target_row = -1

        while row_up <= row_down:
            row_middle = (row_up + row_down) // 2

            if target < matrix[row_middle][column_left]:
                row_down = row_middle - 1
            elif target > matrix[row_middle][column_right]:
                row_up = row_middle + 1
            else:
                target_row = row_middle
                break

        if target_row == -1:
            return False

        while column_left <= column_right:
            column_middle = (column_left + column_right) // 2
            middle_value = matrix[target_row][column_middle]

            if target < middle_value:
                column_right = column_middle - 1
            elif target > middle_value:
                column_left = column_middle + 1
            else:
                return True

        return False


def test_example_1() -> None:
    solution = Solution()
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    actual = solution.searchMatrix(matrix, 10)
    expected = True
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    actual = solution.searchMatrix(matrix, 15)
    expected = False
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
