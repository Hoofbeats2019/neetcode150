"""Unit tests for Clone Graph."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.clone_graph import Node, Solution, example_graph_1, example_graph_2


class TestCloneGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_three_node_graph(self) -> None:
        original = example_graph_1()

        copied = self.solution.cloneGraph(original)

        self.assertIsNotNone(copied)
        assert copied is not None
        self.assertIsNot(copied, original)
        self.assertEqual(copied.val, 1)
        self.assertEqual([neighbor.val for neighbor in copied.neighbors], [2])

        copied_node_2 = copied.neighbors[0]
        self.assertIsNot(copied_node_2, original.neighbors[0])
        self.assertEqual(
            [neighbor.val for neighbor in copied_node_2.neighbors],
            [1, 3],
        )
        self.assertIs(copied_node_2.neighbors[0], copied)
        self.assertIsNot(
            copied_node_2.neighbors[1],
            original.neighbors[0].neighbors[1],
        )

    def test_isolated_node(self) -> None:
        original = example_graph_2()

        copied = self.solution.cloneGraph(original)

        self.assertIsNotNone(copied)
        assert copied is not None
        self.assertIsNot(copied, original)
        self.assertEqual(copied.val, 1)
        self.assertEqual(copied.neighbors, [])

    def test_empty_graph(self) -> None:
        self.assertIsNone(self.solution.cloneGraph(None))

    def test_cycle_does_not_point_back_to_original_nodes(self) -> None:
        node_1 = Node(1)
        node_2 = Node(2)
        node_1.neighbors = [node_2]
        node_2.neighbors = [node_1]

        copied = self.solution.cloneGraph(node_1)

        self.assertIsNotNone(copied)
        assert copied is not None
        copied_node_2 = copied.neighbors[0]
        self.assertIs(copied_node_2.neighbors[0], copied)
        self.assertIsNot(copied_node_2, node_2)
        self.assertIsNot(copied_node_2.neighbors[0], node_1)


if __name__ == "__main__":
    unittest.main()
