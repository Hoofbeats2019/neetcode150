"""Pacific Atlantic Water Flow.

Created: 22 August 2026
Created by: Yanlong Su

You are given a rectangular island ``heights`` where ``heights[r][c]`` is the
height above sea level of the cell at coordinate ``(r, c)``.

The island borders the Pacific Ocean on its top and left sides and the
Atlantic Ocean on its bottom and right sides. Water can flow up, down, left,
or right to a neighboring cell whose height is equal to or lower than the
current cell.

Return every cell from which water can flow to both oceans. The answer may be
returned in any order.

Example 1:
    Input:
        heights = [
            [4, 2, 7, 3, 4],
            [7, 4, 6, 4, 7],
            [6, 3, 5, 3, 6],
        ]
    Output:
        [[0, 2], [0, 4], [1, 0], [1, 1],
         [1, 2], [1, 3], [1, 4], [2, 0]]

Example 2:
    Input: heights = [[1], [1]]
    Output: [[0, 0], [1, 0]]

Constraints:
    1 <= len(heights), len(heights[r]) <= 100
    0 <= heights[r][c] <= 1000

Pseudocode:
    pacificAtlantic(heights):
        collect every top and left border cell for the Pacific
        collect every bottom and right border cell for the Atlantic

        run a depth-first search from each ocean's border cells
        during each reversed search:
            visit top, bottom, left, and right neighbors
            continue only to a neighbor of equal or greater height

        return the intersection of the two visited-cell sets

Time complexity: O(rows * columns)
Space complexity: O(rows * columns)
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Return cells from which water can flow to both oceans."""
        rows = len(heights)
        columns = len(heights[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        pacific_borders = [(row, 0) for row in range(rows)]
        pacific_borders.extend((0, column) for column in range(columns))

        atlantic_borders = [(row, columns - 1) for row in range(rows)]
        atlantic_borders.extend(
            (rows - 1, column) for column in range(columns)
        )

        def dfs_from_ocean(
            border_cells: list[tuple[int, int]],
        ) -> set[tuple[int, int]]:
            """Return cells reachable by a reversed search from one ocean."""
            visited: set[tuple[int, int]] = set()
            stack = border_cells.copy()

            while stack:
                row, column = stack.pop()

                if (row, column) in visited:
                    continue

                visited.add((row, column))

                for row_change, column_change in directions:
                    neighbor_row = row + row_change
                    neighbor_column = column + column_change

                    if not 0 <= neighbor_row < rows:
                        continue

                    if not 0 <= neighbor_column < columns:
                        continue

                    neighbor = (neighbor_row, neighbor_column)
                    if neighbor in visited:
                        continue

                    # Reverse water flow: travel toward equal or higher cells.
                    if heights[neighbor_row][neighbor_column] < heights[row][column]:
                        continue

                    stack.append(neighbor)

            return visited

        pacific_reachable = dfs_from_ocean(pacific_borders)
        atlantic_reachable = dfs_from_ocean(atlantic_borders)

        cells_reaching_both = pacific_reachable & atlantic_reachable
        return [[row, column] for row, column in cells_reaching_both]


def example_heights_1() -> list[list[int]]:
    """Return a fresh copy of the first example island."""
    return [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 4, 7],
        [6, 3, 5, 3, 6],
    ]


def example_heights_2() -> list[list[int]]:
    """Return a fresh copy of the second example island."""
    return [[1], [1]]


def test_example_1() -> None:
    """Run the first worked example."""
    expected = {
        (0, 2),
        (0, 4),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 0),
    }
    actual = {tuple(cell) for cell in Solution().pacificAtlantic(example_heights_1())}
    assert actual == expected


def test_example_2() -> None:
    """Run the second worked example."""
    expected = {(0, 0), (1, 0)}
    actual = {tuple(cell) for cell in Solution().pacificAtlantic(example_heights_2())}
    assert actual == expected


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
