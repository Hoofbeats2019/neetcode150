"""Number of Connected Components in an Undirected Graph.

Created: 23 August 2026
Created by: Yanlong Su

You have an undirected graph of ``n`` nodes labeled from ``0`` to ``n - 1``.
You are given an integer ``n`` and an array ``edges`` where
``edges[i] = [a_i, b_i]`` indicates an edge between ``a_i`` and ``b_i``.

Return the number of connected components in the graph.

Example 1:
    Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
    Output: 2

Example 2:
    Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    Output: 1

Constraints:
    1 <= n <= 2000
    1 <= len(edges) <= 5000
    len(edges[i]) == 2
    0 <= a_i < n
    0 <= b_i < n
    a_i != b_i
    There are no repeated edges.

Pseudocode:
    countComponents(n, edges):
        create an n by n adjacency matrix filled with false
        for each edge [node_1, node_2]:
            mark the connection in both directions

        create a processed array of size n filled with false
        set component count to zero

        dfs(node):
            mark node as processed
            for each possible neighbor:
                if an edge exists and the neighbor is not processed:
                    run DFS from the neighbor

        for each node:
            if the node is not processed:
                increment the component count
                run DFS from the node

        return the component count

Time complexity: O(n^2)
Space complexity: O(n^2)
"""

import sys
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Return the number of connected components in the graph."""
        sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 100))

        adjacency_matrix = [[False] * n for _ in range(n)]

        for node_1, node_2 in edges:
            adjacency_matrix[node_1][node_2] = True
            adjacency_matrix[node_2][node_1] = True

        processed = [False] * n

        def dfs(node: int) -> None:
            processed[node] = True

            for neighbor in range(n):
                if (
                    adjacency_matrix[node][neighbor]
                    and not processed[neighbor]
                ):
                    dfs(neighbor)

        component_count = 0

        for node in range(n):
            if not processed[node]:
                component_count += 1
                dfs(node)

        return component_count


def test_example_1() -> None:
    """Run the first worked example."""
    edges = [[0, 1], [1, 2], [3, 4]]
    assert Solution().countComponents(5, edges) == 2


def test_example_2() -> None:
    """Run the second worked example."""
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert Solution().countComponents(5, edges) == 1


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
