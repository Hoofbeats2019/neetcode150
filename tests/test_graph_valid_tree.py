"""Unit tests for Graph Valid Tree."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.graph_valid_tree import Solution


class TestGraphValidTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_edges_form_a_valid_tree(self) -> None:
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        self.assertTrue(self.solution.validTree(5, edges))

    def test_edges_containing_a_cycle_do_not_form_a_tree(self) -> None:
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        self.assertFalse(self.solution.validTree(5, edges))

    def test_single_node_without_edges_is_a_tree(self) -> None:
        self.assertTrue(self.solution.validTree(1, []))

    def test_disconnected_nodes_do_not_form_a_tree(self) -> None:
        self.assertFalse(self.solution.validTree(4, [[0, 1], [2, 3]]))


if __name__ == "__main__":
    unittest.main()
