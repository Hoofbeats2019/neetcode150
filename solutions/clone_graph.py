"""Clone Graph.

Created: 22 August 2026
Created by: Yanlong Su

Given a node in a connected undirected graph, return a deep copy of the graph.
Each node contains an integer value and a list of its neighbors.

The graph is represented in examples as a 1-indexed adjacency list. Node values
are numbered from 1 to n, and the supplied node is node 1.

Example 1:
    Input: adjList = [[2], [1, 3], [2]]
    Output: [[2], [1, 3], [2]]

Example 2:
    Input: adjList = [[]]
    Output: [[]]

Example 3:
    Input: adjList = []
    Output: []

Constraints:
    0 <= number of nodes <= 100
    1 <= Node.val <= 100
    The graph has no duplicate edges or self-loops.

Approach:
    Traverse the original graph with breadth-first search. Map every original
    node to exactly one copied node. When a neighbor is discovered for the
    first time, create its copy and add the original neighbor to the queue.
    Connect each current copied node to the copies of its original neighbors.

Time complexity: O(V + E)
Space complexity: O(V)
"""

from collections import deque
from typing import Optional


class Node:
    """A node in an undirected graph."""

    def __init__(
        self,
        val: int = 0,
        neighbors: Optional[list["Node"]] = None,
    ) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """Return a deep copy of the connected graph containing node."""
        if node is None:
            return None

        original_to_copy = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            original_node = queue.popleft()
            copied_node = original_to_copy[original_node]

            for original_neighbor in original_node.neighbors:
                if original_neighbor not in original_to_copy:
                    original_to_copy[original_neighbor] = Node(
                        original_neighbor.val
                    )
                    queue.append(original_neighbor)

                copied_node.neighbors.append(
                    original_to_copy[original_neighbor]
                )

        return original_to_copy[node]


def example_graph_1() -> Node:
    """Build the three-node graph from the first example."""
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.neighbors = [node_2]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2]

    return node_1


def example_graph_2() -> Node:
    """Build the isolated node from the second example."""
    return Node(1)


def test_example_1() -> None:
    """Run the first worked example."""
    original = example_graph_1()
    copied = Solution().cloneGraph(original)

    assert copied is not None
    assert copied is not original
    assert copied.val == 1
    assert [neighbor.val for neighbor in copied.neighbors] == [2]
    assert [neighbor.val for neighbor in copied.neighbors[0].neighbors] == [1, 3]


def test_example_2() -> None:
    """Run the second worked example."""
    original = example_graph_2()
    copied = Solution().cloneGraph(original)

    assert copied is not None
    assert copied is not original
    assert copied.val == 1
    assert copied.neighbors == []


def test_example_3() -> None:
    """Run the empty-graph example."""
    assert Solution().cloneGraph(None) is None


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
