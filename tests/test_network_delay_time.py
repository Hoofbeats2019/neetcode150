"""Unit tests for Network Delay Time."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.network_delay_time import Solution


class TestNetworkDelayTime(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_signal_reaches_every_node(self) -> None:
        times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
        self.assertEqual(
            self.solution.networkDelayTime(times, 4, 1),
            3,
        )

    def test_source_cannot_reach_every_node(self) -> None:
        times = [[1, 2, 1], [2, 3, 1]]
        self.assertEqual(
            self.solution.networkDelayTime(times, 3, 2),
            -1,
        )

    def test_single_node_receives_signal_immediately(self) -> None:
        self.assertEqual(
            self.solution.networkDelayTime([[1, 1, 0]], 1, 1),
            0,
        )

    def test_zero_weight_edges_take_no_time(self) -> None:
        times = [[1, 2, 0], [2, 3, 0]]
        self.assertEqual(
            self.solution.networkDelayTime(times, 3, 1),
            0,
        )

    def test_answer_uses_last_node_arrival_time(self) -> None:
        times = [[1, 2, 2], [1, 3, 5]]
        self.assertEqual(
            self.solution.networkDelayTime(times, 3, 1),
            5,
        )


if __name__ == "__main__":
    unittest.main()
