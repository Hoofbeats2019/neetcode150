"""K Closest Points to Origin.

Created: 15 August 2026
Created by: Yanlong Su

You are given an array of points where ``points[i] = [x_i, y_i]`` represents
a point on the Cartesian plane, and an integer ``k``. Return the ``k`` points
closest to the origin ``(0, 0)``.

The distance between two points is their Euclidean distance. The answer may be
returned in any order, and it is guaranteed to be unique except for ordering.

Example 1:
    Input: points = [[0, 2], [2, 2]], k = 1
    Output: [[0, 2]]

Example 2:
    Input: points = [[0, 2], [2, 0], [2, 2]], k = 2
    Output: [[0, 2], [2, 0]]

Constraints:
    1 <= k <= points.length <= 1000
    -1000 <= x_i, y_i <= 1000

Pseudocode:
    kClosest(points, k):
        create an empty heap

        for each point in points:
            x = point[0]
            y = point[1]
            squared_distance = x^2 + y^2

            push (-squared_distance, point) into the heap

            if the size of the heap is greater than k:
                pop from the heap

        return every point stored in the heap
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Return the k points nearest to the origin."""
        heap: list[tuple[int, List[int]]] = []

        for point in points:
            x, y = point
            squared_distance = x**2 + y**2
            heappush(heap, (-squared_distance, point))

            if len(heap) > k:
                heappop(heap)

        return [point for _, point in heap]


def test_example_1() -> None:
    solution = Solution()
    actual = solution.kClosest([[0, 2], [2, 2]], 1)
    expected = [[0, 2]]
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.kClosest([[0, 2], [2, 0], [2, 2]], 2)
    expected = [[0, 2], [2, 0]]
    assert sorted(actual) == sorted(expected), (
        f"Expected {expected} in any order, but received {actual}"
    )


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
