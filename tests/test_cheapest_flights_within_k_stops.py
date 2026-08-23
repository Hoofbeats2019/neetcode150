"""Unit tests for Cheapest Flights Within K Stops."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.cheapest_flights_within_k_stops import Solution


class TestCheapestFlightsWithinKStops(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        flights = [
            [0, 1, 200],
            [1, 2, 100],
            [1, 3, 300],
            [2, 3, 100],
        ]
        self.assertEqual(
            self.solution.findCheapestPrice(4, flights, 0, 3, 1),
            500,
        )

    def test_second_worked_example(self) -> None:
        flights = [[1, 0, 100], [1, 2, 200], [0, 2, 100]]
        self.assertEqual(
            self.solution.findCheapestPrice(3, flights, 1, 2, 1),
            200,
        )

    def test_zero_stops_allows_a_direct_flight_only(self) -> None:
        flights = [[0, 1, 20], [1, 2, 20], [0, 2, 100]]
        self.assertEqual(
            self.solution.findCheapestPrice(3, flights, 0, 2, 0),
            100,
        )

    def test_cheaper_route_is_used_when_stop_limit_allows_it(self) -> None:
        flights = [[0, 1, 20], [1, 2, 20], [0, 2, 100]]
        self.assertEqual(
            self.solution.findCheapestPrice(3, flights, 0, 2, 1),
            40,
        )

    def test_route_with_too_many_stops_is_rejected(self) -> None:
        flights = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [0, 3, 100]]
        self.assertEqual(
            self.solution.findCheapestPrice(4, flights, 0, 3, 1),
            100,
        )

    def test_unreachable_destination_returns_negative_one(self) -> None:
        flights = [[0, 1, 50], [2, 3, 50]]
        self.assertEqual(
            self.solution.findCheapestPrice(4, flights, 0, 3, 2),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
