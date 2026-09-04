"""Detect Squares.

Created: 4 September 2026
Created by: Yanlong Su

Maintain a stream of points on a 2-D plane. Duplicate points are separate
points and can be used in separate ways to form a square.

Implement ``CountSquares``:

- ``add(point)`` adds ``point = [x, y]`` to the stream.
- ``count(point)`` returns the number of ways to choose three stored points
  that, together with ``point``, form an axis-aligned square.

Example 1:
    Input:
        add([1, 1])
        add([2, 2])
        add([1, 2])
        count([2, 1])
    Output: 1

    After adding another [2, 2], count([2, 1]) returns 2 because the two
    copies of [2, 2] produce two distinct choices.

Constraints:
    point has length 2
    0 <= x, y <= 1000

Pseudocode:
    count(query_point):
        for each stored point on the query point's vertical line:
            calculate the non-zero side length

            for both horizontal directions:
                calculate the two remaining corner coordinates
                multiply the frequencies of all three required stored points
                add that product to the total

Time complexity: O(u) per count, where u is the number of distinct stored
    coordinates.
Space complexity: O(u), where u is the number of distinct stored coordinates.
"""

from collections import defaultdict
from typing import DefaultDict


class CountSquares:
    """Store point frequencies and count axis-aligned squares."""

    def __init__(self) -> None:
        self.points: DefaultDict[tuple[int, int], int] = defaultdict(int)

    def add(self, point: list[int]) -> None:
        """Add one occurrence of a point to the stream."""
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: list[int]) -> int:
        """Count squares that use ``point`` as one corner."""
        query_x, query_y = point
        total_squares = 0

        for (stored_x, stored_y), vertical_count in self.points.items():
            if stored_x != query_x or stored_y == query_y:
                continue

            side_length = abs(stored_y - query_y)

            for horizontal_direction in (-1, 1):
                other_x = query_x + horizontal_direction * side_length
                total_squares += (
                    vertical_count
                    * self.points.get((other_x, query_y), 0)
                    * self.points.get((other_x, stored_y), 0)
                )

        return total_squares


def test_worked_example() -> None:
    """Run the supplied worked example."""
    count_squares = CountSquares()
    count_squares.add([1, 1])
    count_squares.add([2, 2])
    count_squares.add([1, 2])

    assert count_squares.count([2, 1]) == 1
    assert count_squares.count([3, 3]) == 0

    count_squares.add([2, 2])
    assert count_squares.count([2, 1]) == 2


if __name__ == "__main__":
    test_worked_example()
    print("The worked example passed.")
