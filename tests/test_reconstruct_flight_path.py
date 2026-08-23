"""Unit tests for Reconstruct Flight Path."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.reconstruct_flight_path import Solution


class TestReconstructFlightPath(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_linear_flight_path(self) -> None:
        tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
        expected = ["JFK", "BUF", "HOU", "SEA"]
        self.assertEqual(self.solution.findItinerary(tickets), expected)

    def test_lexicographically_smallest_flight_path(self) -> None:
        tickets = [
            ["HOU", "JFK"],
            ["SEA", "JFK"],
            ["JFK", "SEA"],
            ["JFK", "HOU"],
        ]
        expected = ["JFK", "HOU", "JFK", "SEA", "JFK"]
        self.assertEqual(self.solution.findItinerary(tickets), expected)

    def test_single_ticket(self) -> None:
        self.assertEqual(
            self.solution.findItinerary([["JFK", "SFO"]]),
            ["JFK", "SFO"],
        )

    def test_duplicate_tickets_are_each_used_once(self) -> None:
        tickets = [["JFK", "ATL"], ["JFK", "ATL"], ["ATL", "JFK"]]
        expected = ["JFK", "ATL", "JFK", "ATL"]
        self.assertEqual(self.solution.findItinerary(tickets), expected)

    def test_early_dead_end_is_placed_at_end(self) -> None:
        tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        expected = ["JFK", "NRT", "JFK", "KUL"]
        self.assertEqual(self.solution.findItinerary(tickets), expected)


if __name__ == "__main__":
    unittest.main()
