"""Min Cost to Connect Points.

Created: 23 August 2026
Created by: Yanlong Su

You are given an array ``points`` containing distinct integer coordinates on a
2D plane, where ``points[i] = [x_i, y_i]``.

The cost of connecting two points is their Manhattan distance:
``abs(x_i - x_j) + abs(y_i - y_j)``.

Return the minimum total cost required to connect every point. All points are
connected when there is exactly one simple path between each pair of points.

Example 1:
    Input: points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    Output: 20

Example 2:
    Input: points = [[3, 12], [-2, 5], [-4, 1]]
    Output: 18

Constraints:
    1 <= len(points) <= 1000
    len(points[i]) == 2
    -10^6 <= x_i, y_i <= 10^6
    All coordinate pairs are distinct.

Pseudocode:
    minCostConnectPoints(points):
        create every edge between two different points
        calculate each edge cost using Manhattan distance
        sort all edges from smallest to largest cost

        create a Union-Find with each point in its own group
        set the total cost and selected edge count to zero

        for each edge in sorted order:
            find the group containing each endpoint
            if the endpoints are already in the same group:
                skip the edge because it would create a cycle

            merge the endpoint groups
            add the edge cost to the total
            stop after selecting len(points) - 1 edges

        return the total cost

Time complexity: O(n^2 log n)
Space complexity: O(n^2)
"""

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Return the minimum total cost needed to connect every point."""
        point_count = len(points)
        edges: list[tuple[int, int, int]] = []

        # The graph is complete, so create one edge for every pair of points.
        for point_1 in range(point_count):
            x_1, y_1 = points[point_1]

            for point_2 in range(point_1 + 1, point_count):
                x_2, y_2 = points[point_2]
                distance = abs(x_1 - x_2) + abs(y_1 - y_2)
                edges.append((distance, point_1, point_2))

        edges.sort()

        # Union-Find tracks connectivity using only edges selected for the MST.
        parents = list(range(point_count))
        ranks = [0] * point_count

        def find(point: int) -> int:
            """Return the representative of point's selected-edge group."""
            if parents[point] != point:
                parents[point] = find(parents[point])

            return parents[point]

        def union(point_1: int, point_2: int) -> bool:
            """Merge two groups, returning whether a merge was required."""
            root_1 = find(point_1)
            root_2 = find(point_2)

            if root_1 == root_2:
                return False

            if ranks[root_1] < ranks[root_2]:
                parents[root_1] = root_2
            elif ranks[root_1] > ranks[root_2]:
                parents[root_2] = root_1
            else:
                parents[root_2] = root_1
                ranks[root_1] += 1

            return True

        total_cost = 0
        selected_edges = 0

        for cost, point_1, point_2 in edges:
            # Points already in the same group have a selected path between
            # them, so adding this edge would create a cycle.
            if not union(point_1, point_2):
                continue

            total_cost += cost
            selected_edges += 1

            if selected_edges == point_count - 1:
                break

        return total_cost


def test_example_1() -> None:
    """Run the first worked example."""
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert Solution().minCostConnectPoints(points) == 20


def test_example_2() -> None:
    """Run the second worked example."""
    points = [[3, 12], [-2, 5], [-4, 1]]
    assert Solution().minCostConnectPoints(points) == 18


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
