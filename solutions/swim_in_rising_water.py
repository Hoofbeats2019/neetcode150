"""Swim in Rising Water.

Created: 23 August 2026
Created by: Yanlong Su

You are given a square 2-D matrix of distinct integers ``grid`` where each
integer ``grid[row][column]`` represents the elevation at that position.

Rain starts at time zero, and the water level across the entire grid is equal
to the current time. You may swim horizontally or vertically between adjacent
cells when both elevations are less than or equal to the water level.

Starting from the top-left cell ``(0, 0)``, return the minimum time required
to reach the bottom-right cell ``(n - 1, n - 1)``.

Example 1:
    Input: grid = [[0, 1], [2, 3]]
    Output: 3
    Explanation: The water level must reach 3 before the destination can be
    entered.

Example 2:
    Input:
        grid = [
            [0, 1, 2, 10],
            [9, 14, 4, 13],
            [12, 3, 8, 15],
            [11, 5, 7, 6],
        ]
    Output: 8
    Explanation: At time 8, the path with elevations
    [0, 1, 2, 4, 8, 7, 6] becomes available.

Constraints:
    len(grid) == len(grid[row])
    1 <= len(grid) <= 50
    0 <= grid[row][column] < n^2
    Every elevation is distinct.

Pseudocode:
    swimInWater(grid):
        store the starting cell in a min-heap
        set its best known time to its elevation

        while the min-heap is not empty:
            remove the cell with the smallest required time
            skip the entry if a better time was already found
            return its time if it is the bottom-right cell

            for each horizontal and vertical neighbor inside the grid:
                next time = maximum of the current time and neighbor elevation
                if next time improves the neighbor's best known time:
                    update the neighbor and add it to the min-heap

Time complexity: O(n^2 log n)
Space complexity: O(n^2)
"""

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Return the earliest time the bottom-right cell can be reached."""
        size = len(grid)
        infinity = float("inf")
        best_times = [
            [infinity] * size
            for _ in range(size)
        ]
        best_times[0][0] = grid[0][0]

        min_heap = [(grid[0][0], 0, 0)]
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while min_heap:
            time, row, column = heapq.heappop(min_heap)

            if time > best_times[row][column]:
                continue

            if row == size - 1 and column == size - 1:
                return time

            for row_change, column_change in directions:
                next_row = row + row_change
                next_column = column + column_change

                if not 0 <= next_row < size:
                    continue

                if not 0 <= next_column < size:
                    continue

                next_time = max(time, grid[next_row][next_column])

                if next_time >= best_times[next_row][next_column]:
                    continue

                best_times[next_row][next_column] = next_time
                heapq.heappush(
                    min_heap,
                    (next_time, next_row, next_column),
                )

        raise RuntimeError("The bottom-right cell should always be reachable.")


def example_grid_1() -> list[list[int]]:
    """Return a fresh copy of the first example grid."""
    return [[0, 1], [2, 3]]


def example_grid_2() -> list[list[int]]:
    """Return a fresh copy of the second example grid."""
    return [
        [0, 1, 2, 10],
        [9, 14, 4, 13],
        [12, 3, 8, 15],
        [11, 5, 7, 6],
    ]


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().swimInWater(example_grid_1()) == 3


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().swimInWater(example_grid_2()) == 8


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
