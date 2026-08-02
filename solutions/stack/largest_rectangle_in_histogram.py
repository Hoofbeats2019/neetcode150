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

        stack = []

        for index in range(number_of_bars - 1, -1, -1):
            height = heights[index]

            while stack and heights[stack[-1]] >= height:
                stack.pop()

            if stack:
                index_finish_right[index] = stack[-1] - 1

            stack.append(index)

        maximum_area = 0

        for index, height in enumerate(heights):
            left = index_start_left[index]
            right = index_finish_right[index]
            width = right - left + 1
            maximum_area = max(maximum_area, height * width)

        return maximum_area
