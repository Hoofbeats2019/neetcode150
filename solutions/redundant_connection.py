"""Redundant Connection.

Created: 23 August 2026
Created by: Yanlong Su

You are given a connected undirected graph with ``n`` nodes labeled from 1 to
``n``. The graph originally contained no cycles and had ``n - 1`` edges. One
additional edge, which connects two different vertices and did not previously
exist, has been added.

The graph is represented by an array ``edges`` of length ``n``, where
``edges[i] = [a_i, b_i]`` represents an undirected edge between nodes ``a_i``
and ``b_i``.

Return an edge that can be removed so that the graph remains connected and has
no cycles. If multiple answers are possible, return the edge that appears last
in ``edges``.

Example 1:
    Input: edges = [[1, 2], [1, 3], [3, 4], [2, 4]]
    Output: [2, 4]

Example 2:
    Input: edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    Output: [3, 4]

Constraints:
    n == len(edges)
    3 <= n <= 1000
    1 <= edges[i][0] < edges[i][1] <= len(edges)
    There are no repeated edges and no self-loops.

Pseudocode:
    findRedundantConnection(edges):
        build an undirected adjacency matrix from edges
        create an empty DFS path and an empty set of cycle edges

        dfs(node, parent):
            mark node as visiting and add it to the current path
            for every node connected to node:
                skip the edge leading back to parent
                recursively visit an unvisited neighbor
                if a neighbor is already on the current path:
                    collect every edge from that neighbor to the end of the path
                    include the edge from the current node back to that neighbor
                    report that the cycle was found
            remove node from the path and mark it visited

        run DFS from node 1
        scan edges backward and return the first edge that belongs to the cycle

Time complexity: O(n^2)
Space complexity: O(n^2)
"""

import sys
from typing import List


class Solution:
    def findRedundantConnection(
        self,
        edges: List[List[int]],
    ) -> List[int]:
        """Return the last removable edge that restores a tree."""
        node_count = len(edges)
        sys.setrecursionlimit(
            max(sys.getrecursionlimit(), node_count + 100)
        )

        # Node labels start at 1, so row and column 0 remain unused.
        # The matrix records every undirected edge in both directions.
        adjacency_matrix = [
            [False] * (node_count + 1)
            for _ in range(node_count + 1)
        ]

        for node_1, node_2 in edges:
            adjacency_matrix[node_1][node_2] = True
            adjacency_matrix[node_2][node_1] = True

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * (node_count + 1)

        # `path` contains the active DFS branch. Storing each node's index in
        # that path lets us reconstruct the cycle when we find a back edge.
        path: list[int] = []
        path_positions = [-1] * (node_count + 1)
        cycle_edges: set[tuple[int, int]] = set()

        def normalize_edge(node_1: int, node_2: int) -> tuple[int, int]:
            """Represent an undirected edge independently of endpoint order."""
            return min(node_1, node_2), max(node_1, node_2)

        def dfs(node: int, parent: int) -> bool:
            """Find the cycle and record each edge that belongs to it."""
            states[node] = visiting
            path_positions[node] = len(path)
            path.append(node)

            for neighbor in range(1, node_count + 1):
                if not adjacency_matrix[node][neighbor]:
                    continue

                # In an undirected graph, every tree edge also points back to
                # the parent. That reverse direction does not form a cycle.
                if neighbor == parent:
                    continue

                if states[neighbor] == unvisited:
                    if dfs(neighbor, node):
                        return True
                elif states[neighbor] == visiting:
                    # A visiting neighbor is already on the active path. The
                    # path segment from it to this node, plus this back edge,
                    # contains exactly the edges in the cycle.
                    cycle_start = path_positions[neighbor]

                    for index in range(cycle_start, len(path) - 1):
                        cycle_edges.add(
                            normalize_edge(path[index], path[index + 1])
                        )

                    cycle_edges.add(normalize_edge(node, neighbor))
                    return True

            # No cycle was found through this node, so remove it from the
            # active branch and mark its search as complete.
            path.pop()
            path_positions[node] = -1
            states[node] = visited
            return False

        dfs(1, -1)

        # Any cycle edge can be removed. Scanning backward selects the one
        # appearing last in the original input, as required by the problem.
        for node_1, node_2 in reversed(edges):
            if normalize_edge(node_1, node_2) in cycle_edges:
                return [node_1, node_2]

        # The constraints guarantee one redundant edge, so this is a safeguard
        # for inputs outside the stated problem conditions.
        return []


def test_example_1() -> None:
    """Run the first worked example."""
    edges = [[1, 2], [1, 3], [3, 4], [2, 4]]
    assert Solution().findRedundantConnection(edges) == [2, 4]


def test_example_2() -> None:
    """Run the second worked example."""
    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    assert Solution().findRedundantConnection(edges) == [3, 4]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
