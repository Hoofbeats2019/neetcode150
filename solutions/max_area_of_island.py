"""Max Area of Island.

Created: 22 August 2026
Created by: Yanlong Su

You are given a matrix ``grid`` where each cell is either ``0`` (water) or
``1`` (land).

An island is a group of ``1`` cells connected horizontally or vertically. All
four edges of the grid are surrounded by water. The area of an island is the
number of cells within it.

Return the maximum area of an island in ``grid``. If no island exists, return
``0``.

Example 1:
    Input:
        grid = [
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1],
        ]
    Output: 6

    Explanation: Land cells cannot be connected diagonally, so the maximum
    island area is 6.

Example 2:
    Input:
        grid = [[0]]
    Output: 0

Constraints:
    1 <= len(grid), len(grid[i]) <= 50
    ``grid[i][j]`` is ``0`` or ``1``.

Pseudocode:
    maxAreaOfIsland(grid):
        use the same connected-component traversal as Number of Islands
        add every land position to an unvisited-land set
        set maximum area to zero

        while unvisited land remains:
            choose any unvisited land node
            set the current island area to zero
            add that node to a traversal stack

            while the stack is not empty:
                remove the last node from the stack
                skip it if it is no longer unvisited
                remove it from the unvisited-land set
                increment the current island area

                for each top, bottom, left, and right neighbor:
                    if the neighbor is unvisited land:
                        add it to the stack

            instead of incrementing a component count, update maximum area
            with the current component's area

        return maximum area

Time complexity: O(rows * columns)
Space complexity: O(rows * columns)
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Return the largest area among the islands in grid."""
        unvisited_land: set[tuple[int, int]] = set()

        # Treat every land cell as a node in the graph.
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    unvisited_land.add((row, column))

        maximum_area = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # Each outer iteration processes one complete connected component.
        while unvisited_land:
            start_node = next(iter(unvisited_land))
            current_area = 0
            stack = [start_node]

            while stack:
                row, column = stack.pop()

                if (row, column) not in unvisited_land:
                    continue

                unvisited_land.remove((row, column))
                current_area += 1

                for row_change, column_change in directions:
                    neighbor = (row + row_change, column + column_change)

                    if neighbor in unvisited_land:
                        stack.append(neighbor)

            maximum_area = max(maximum_area, current_area)

        return maximum_area


def example_grid_1() -> list[list[int]]:
    """Return a fresh copy of the first example grid."""
    return [
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
    ]


def example_grid_2() -> list[list[int]]:
    """Return a fresh copy of the second example grid."""
    return [[0]]


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().maxAreaOfIsland(example_grid_1()) == 6


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().maxAreaOfIsland(example_grid_2()) == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
