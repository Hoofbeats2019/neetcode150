"""Unit tests for Number of Connected Components in an Undirected Graph."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.number_of_connected_components_in_an_undirected_graph import (
    Solution,
)


class TestNumberOfConnectedComponentsInAnUndirectedGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_graph_with_two_components(self) -> None:
        edges = [[0, 1], [1, 2], [3, 4]]
        self.assertEqual(self.solution.countComponents(5, edges), 2)

    def test_fully_connected_graph(self) -> None:
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.solution.countComponents(5, edges), 1)

    def test_nodes_without_edges_are_separate_components(self) -> None:
        self.assertEqual(self.solution.countComponents(4, [[0, 1]]), 3)


if __name__ == "__main__":
    unittest.main()
