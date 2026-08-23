"""Cheapest Flights Within K Stops.

Created: 23 August 2026
Created by: Yanlong Su

There are ``n`` airports labeled from ``0`` to ``n - 1``. Each entry
``[from_i, to_i, price_i]`` in ``flights`` represents a one-way flight from
airport ``from_i`` to airport ``to_i`` with cost ``price_i``.

Given a starting airport ``src``, a destination airport ``dst``, and a maximum
number of stops ``k``, return the cheapest price from ``src`` to ``dst`` using
at most ``k`` stops. Return ``-1`` when no such route exists.

Example 1:
    Input:
        n = 4
        flights = [[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]]
        src = 0
        dst = 3
        k = 1
    Output: 500
    Explanation: The route 0 -> 1 -> 3 costs 500 and uses one stop. The
    cheaper route 0 -> 1 -> 2 -> 3 uses two stops, so it is not allowed.

Example 2:
    Input:
        n = 3
        flights = [[1, 0, 100], [1, 2, 200], [0, 2, 100]]
        src = 1
        dst = 2
        k = 1
    Output: 200

Constraints:
    Airports are labeled from ``0`` through ``n - 1``
    Each flight is a directed edge ``[from_i, to_i, price_i]``
    There are no duplicate flights
    No flight starts and ends at the same airport
    src != dst
    k is the maximum number of intermediate stops

Pseudocode:
    findCheapestPrice(n, flights, src, dst, k):
        create a DP table with k + 2 rows and n columns, filled with infinity
        set the source cost in row zero to zero

        for flight count from 1 through k + 1:
            copy the preceding row into the current row

            for each directed flight from source airport to target airport:
                if the source airport was reachable in the preceding row:
                    add the flight price to its preceding cost
                    keep the smaller cost for the target in the current row

        return -1 if the destination in the last row is infinity
        otherwise return its stored cost

Time complexity: O((k + 1) x (n + E))
Space complexity: O((k + 2) x n)
"""

from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        """Return the cheapest valid flight price, or -1 if unreachable."""
        infinity = float("inf")

        # costs[flight_count][airport] is the cheapest cost from src to the
        # airport using at most flight_count flights.
        costs = [
            [infinity] * n
            for _ in range(k + 2)
        ]
        costs[0][src] = 0

        # At most k stops means taking at most k + 1 flights.
        for flight_count in range(1, k + 2):
            costs[flight_count] = costs[flight_count - 1].copy()        #A DEEP COPY IS REQUIRED HERE, NOT A SHALLOW COPY'

            for source, target, price in flights:
                previous_cost = costs[flight_count - 1][source]

                if previous_cost == infinity:       # UNREACHABLE SOURCE AIRPORT, SKIP THIS FLIGHT
                    continue

                costs[flight_count][target] = min(  # REACHABLE TARGET AIRPORT, UPDATE CHEAPEST COST
                    costs[flight_count][target],    # A LOT OF CLACULATIONS HERE, BUT THE IDEA IS TO KEEP TRACK OF THE CHEAPEST COST TO REACH EACH AIRPORT WITHIN THE ALLOWED NUMBER OF FLIGHTS
                    previous_cost + price,
                )

        cheapest_price = costs[k + 1][dst]

        if cheapest_price == infinity:
            return -1

        return cheapest_price


def test_example_1() -> None:
    """Run the first worked example."""
    flights = [
        [0, 1, 200],
        [1, 2, 100],
        [1, 3, 300],
        [2, 3, 100],
    ]
    assert Solution().findCheapestPrice(4, flights, 0, 3, 1) == 500


def test_example_2() -> None:
    """Run the second worked example."""
    flights = [[1, 0, 100], [1, 2, 200], [0, 2, 100]]
    assert Solution().findCheapestPrice(3, flights, 1, 2, 1) == 200


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
