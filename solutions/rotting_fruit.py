"""Rotting Fruit.

Created: 22 August 2026
Created by: Yanlong Su

You are given a 2-D matrix ``grid``. Each cell contains one of three values:

- ``0`` represents an empty cell.
- ``1`` represents a fresh fruit.
- ``2`` represents a rotten fruit.

Every minute, a fresh fruit becomes rotten if it is horizontally or vertically
adjacent to a rotten fruit.

Return the minimum number of minutes that must elapse until no fresh fruit
remains. If this is impossible, return ``-1``.

Example 1:
    Input:
        grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
    Output: 4

Example 2:
    Input:
        grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
    Output: -1

Constraints:
    1 <= len(grid), len(grid[i]) <= 10
    ``grid[i][j]`` is ``0``, ``1``, or ``2``.

Pseudocode:
    orangesRotting(grid):
        add every rotten fruit position to the queue
        set elapsed minutes to zero

        while the queue is not empty:
            create an empty queue for the next minute

            process every rotten fruit in the current queue:
                for each top, bottom, left, and right neighbor:
                    if the neighbor is fresh fruit:
                        change it to rotten fruit
                        add it to the next-minute queue

            if no fruit became rotten, stop the traversal
            replace the current queue with the next-minute queue
            increment elapsed minutes

        if any fresh fruit remains, return -1
        return elapsed minutes

Time complexity: O(rows * columns)
Space complexity: O(rows * columns)
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Return the minimum minutes needed for every fresh fruit to rot."""
        queue: deque[tuple[int, int]] = deque()

        # Start the breadth-first search from every rotten fruit.
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 2:
                    queue.append((row, column))

        minutes = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while queue:
            next_queue: deque[tuple[int, int]] = deque()

            # Every fruit currently queued spreads rot during the same minute.
            while queue:
                row, column = queue.popleft()

                for row_change, column_change in directions:
                    neighbor_row = row + row_change
                    neighbor_column = column + column_change

                    if not 0 <= neighbor_row < len(grid):
                        continue

                    if not 0 <= neighbor_column < len(grid[neighbor_row]):
                        continue

                    if grid[neighbor_row][neighbor_column] != 1:
                        continue

                    grid[neighbor_row][neighbor_column] = 2
                    next_queue.append((neighbor_row, neighbor_column))

            if not next_queue:
                break

            queue = next_queue
            minutes += 1

        for row in grid:
            if 1 in row:
                return -1

        return minutes


def example_grid_1() -> list[list[int]]:
    """Return a fresh copy of the first example grid."""
    return [[1, 1, 0], [0, 1, 1], [0, 1, 2]]


def example_grid_2() -> list[list[int]]:
    """Return a fresh copy of the second example grid."""
    return [[1, 0, 1], [0, 2, 0], [1, 0, 1]]


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().orangesRotting(example_grid_1()) == 4


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().orangesRotting(example_grid_2()) == -1


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
