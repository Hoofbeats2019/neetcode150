"""Islands and Treasure.

Created: 22 August 2026
Created by: Yanlong Su

You are given an ``m x n`` grid containing land cells, water cells, and
treasure chests:

- ``-1`` represents a water cell that cannot be traversed.
- ``0`` represents a treasure chest.
- ``INF`` represents a traversable land cell, where
  ``INF = 2**31 - 1 = 2147483647``.

Fill each land cell with its distance to the nearest treasure chest. Movement
is allowed only horizontally or vertically. If a treasure chest cannot be
reached from a land cell, leave that cell unchanged.

Modify ``grid`` in place and return nothing.

Example 1:
    Input:
        grid = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    Output:
        [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ]

Example 2:
    Input:
        grid = [[0, -1], [2147483647, 2147483647]]
    Output:
        grid = [[0, -1], [1, 2]]

Constraints:
    ``m == len(grid)``
    ``n == len(grid[i])``
    1 <= m, n <= 100
    ``grid[i][j]`` is ``-1``, ``0``, or ``2147483647``.

Pseudocode:
    islandsAndTreasure(grid):
        create an empty queue
        add every treasure position to the queue

        while the queue is not empty:
            remove the position at the front of the queue

            for each top, bottom, left, and right neighbor:
                skip the neighbor if it is outside the grid
                skip the neighbor if it is not unvisited land
                set its distance to the current distance plus one
                add the neighbor to the queue

Time complexity: O(m * n)
Space complexity: O(m * n)
"""

from collections import deque
from typing import List


INF = 2**31 - 1


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """Fill each land cell with its distance to the nearest treasure."""
        queue: deque[tuple[int, int]] = deque()

        # Start the breadth-first search from every treasure simultaneously.
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 0:
                    queue.append((row, column))

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while queue:
            row, column = queue.popleft()

            for row_change, column_change in directions:
                neighbor_row = row + row_change
                neighbor_column = column + column_change

                if not 0 <= neighbor_row < len(grid):
                    continue

                if not 0 <= neighbor_column < len(grid[neighbor_row]):
                    continue

                if grid[neighbor_row][neighbor_column] != INF:
                    continue

                grid[neighbor_row][neighbor_column] = grid[row][column] + 1
                queue.append((neighbor_row, neighbor_column))


def example_grid_1() -> list[list[int]]:
    """Return a fresh copy of the first example grid."""
    return [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]


def example_grid_2() -> list[list[int]]:
    """Return a fresh copy of the second example grid."""
    return [[0, -1], [INF, INF]]


def test_example_1() -> None:
    """Run the first worked example."""
    grid = example_grid_1()
    Solution().islandsAndTreasure(grid)
    assert grid == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]


def test_example_2() -> None:
    """Run the second worked example."""
    grid = example_grid_2()
    Solution().islandsAndTreasure(grid)
    assert grid == [[0, -1], [1, 2]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
