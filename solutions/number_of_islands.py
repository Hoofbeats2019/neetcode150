"""Number of Islands.

Created: 22 August 2026
Created by: Yanlong Su

Given a 2-D grid ``grid`` where ``"1"`` represents land and ``"0"``
represents water, return the number of islands.

An island is formed by horizontally or vertically adjacent land cells and is
surrounded by water. Water surrounds the grid.

Example 1:
    Input:
        grid = [
            ["0", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    Output: 1

Example 2:
    Input:
        grid = [
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    Output: 4

Constraints:
    1 <= len(grid), len(grid[i]) <= 100
    ``grid[i][j]`` is ``"0"`` or ``"1"``.

Pseudocode:
    numIslands(grid):
        add every land position to an unvisited-land set
        set island count to zero

        while unvisited land remains:
            choose any unvisited land node
            increment the island count
            add that node to a traversal stack

            while the stack is not empty:
                remove the last node from the stack
                skip it if it is no longer unvisited
                remove it from the unvisited-land set

                for each top, bottom, left, and right neighbor:
                    if the neighbor is unvisited land:
                        add it to the stack

        return the island count

Time complexity: O(rows * columns)
Space complexity: O(rows * columns)
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Return the number of horizontally or vertically connected islands."""
        unvisited_land: set[tuple[int, int]] = set()

        # Treat every land cell as a node in the graph.
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == "1":
                    unvisited_land.add((row, column))

        island_count = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # Each outer iteration processes one complete connected component.
        while unvisited_land:
            start_node = next(iter(unvisited_land))
            island_count += 1
            stack = [start_node]

            while stack:
                row, column = stack.pop()

                if (row, column) not in unvisited_land:
                    continue

                unvisited_land.remove((row, column))

                for row_change, column_change in directions:
                    neighbor = (row + row_change, column + column_change)

                    if neighbor in unvisited_land:
                        stack.append(neighbor)

        return island_count


def example_grid_1() -> list[list[str]]:
    """Return a fresh copy of the first example grid."""
    return [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]


def example_grid_2() -> list[list[str]]:
    """Return a fresh copy of the second example grid."""
    return [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().numIslands(example_grid_1()) == 1


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().numIslands(example_grid_2()) == 4


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
