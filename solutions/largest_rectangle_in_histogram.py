"""Largest Rectangle in Histogram.

Created: 2 August 2026
Created by: Yanlong Su

You are given an array of integers ``heights`` where ``heights[i]`` represents
the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

This chart is known as a histogram.

Example 1:
    Input: heights = [7, 1, 7, 2, 2, 4]
    Output: 8

Example 2:
    Input: heights = [1, 3, 7]
    Output: 7

Executable examples:
    >>> solution = Solution()
    >>> solution.largestRectangleArea([7, 1, 7, 2, 2, 4])
    8
    >>> solution.largestRectangleArea([1, 3, 7])
    7

Constraints:
    1 <= heights.length <= 1000
    0 <= heights[i] <= 1000
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        number_of_bars = len(heights)
        index_start_left = [0] * number_of_bars
        index_finish_right = [number_of_bars - 1] * number_of_bars

        stack = []

        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                stack.pop()

            if stack:
                index_start_left[index] = stack[-1] + 1

            stack.append(index)

        # print(index_start_left)

        stack = []

        for index in range(number_of_bars - 1, -1, -1):
            height = heights[index]

            while stack and heights[stack[-1]] >= height:
                stack.pop()

            if stack:
                index_finish_right[index] = stack[-1] - 1

            stack.append(index)

        # print(index_finish_right)

        maximum_area = 0

        for index, height in enumerate(heights):
            left = index_start_left[index]
            right = index_finish_right[index]
            width = right - left + 1
            maximum_area = max(maximum_area, height * width)

        return maximum_area


def test_example_1() -> None:
    solution = Solution()
    actual = solution.largestRectangleArea([7, 1, 7, 2, 2, 4])
    expected = 8
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.largestRectangleArea([1, 3, 7])
    expected = 7
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
