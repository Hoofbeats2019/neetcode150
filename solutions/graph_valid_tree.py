"""Graph Valid Tree.

Created: 23 August 2026
Created by: Yanlong Su

Given ``n`` nodes labeled from ``0`` to ``n - 1`` and a list of undirected
edges, return ``True`` when the edges make up a valid tree. Otherwise, return
``False``.

Each edge is a pair of node labels. Duplicate edges do not appear, and because
the edges are undirected, ``[0, 1]`` and ``[1, 0]`` are considered the same
edge.

Example 1:
    Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    Output: True

Example 2:
    Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    Output: False

Pseudocode:
    validTree(n, edges):
        build an undirected adjacency list from edges
        create an empty visited set

        dfs(node, parent):
            return false if node was already visited
            add node to visited
            for each neighbor of node:
                skip the edge leading back to parent
                return false if DFS from the neighbor finds a cycle
            return true

        run DFS from node 0 with no parent
        return false if DFS finds a cycle
        return whether every node was visited

Time complexity: O(V + E)
Space complexity: O(V + E)
"""

import sys
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """Return whether the undirected edges form a valid tree."""
        sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 100))

        adjacency_list: list[list[int]] = [[] for _ in range(n)]

        for node_1, node_2 in edges:
            adjacency_list[node_1].append(node_2)
            adjacency_list[node_2].append(node_1)

        visited: set[int] = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n


def test_example_1() -> None:
    """Run the first worked example."""
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    assert Solution().validTree(5, edges) is True


def test_example_2() -> None:
    """Run the second worked example."""
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    assert Solution().validTree(5, edges) is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
