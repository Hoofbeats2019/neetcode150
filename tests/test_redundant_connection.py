"""Unit tests for Redundant Connection."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.redundant_connection import Solution


class TestRedundantConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_cycle_closes_on_last_edge(self) -> None:
        edges = [[1, 2], [1, 3], [3, 4], [2, 4]]
        self.assertEqual(
            self.solution.findRedundantConnection(edges),
            [2, 4],
        )

    def test_cycle_closes_before_a_tail_edge(self) -> None:
        edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
        self.assertEqual(
            self.solution.findRedundantConnection(edges),
            [3, 4],
        )

    def test_three_node_cycle(self) -> None:
        edges = [[1, 2], [1, 3], [2, 3]]
        self.assertEqual(
            self.solution.findRedundantConnection(edges),
            [2, 3],
        )

    def test_later_cycle_edge_is_returned(self) -> None:
        edges = [[1, 2], [2, 3], [1, 3], [3, 4]]
        self.assertEqual(
            self.solution.findRedundantConnection(edges),
            [1, 3],
        )


if __name__ == "__main__":
    unittest.main()
