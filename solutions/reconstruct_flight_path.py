"""Reconstruct Flight Path.

Created: 23 August 2026
Created by: Yanlong Su

You are given a list of flight tickets where ``tickets[i] = [from_i, to_i]``
represents a flight from one airport to another. Each airport code contains
three uppercase English letters.

Reconstruct and return the itinerary in travel order. The itinerary must start
at ``"JFK"`` and use every ticket exactly once. If more than one valid flight
path exists, return the lexicographically smallest one.

Example 1:
    Input: tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
    Output: ["JFK", "BUF", "HOU", "SEA"]

Example 2:
    Input:
        tickets = [
            ["HOU", "JFK"],
            ["SEA", "JFK"],
            ["JFK", "SEA"],
            ["JFK", "HOU"],
        ]
    Output: ["JFK", "HOU", "JFK", "SEA", "JFK"]
    Explanation:
        ["JFK", "SEA", "JFK", "HOU", "JFK"] is also valid, but it is
        lexicographically larger.

Constraints:
    1 <= len(tickets) <= 300
    tickets[i] contains exactly two airport codes
    Each airport code contains three uppercase English letters
    from_i != to_i
    The tickets form at least one valid flight path starting at ``"JFK"``

Pseudocode:
    findItinerary(tickets):
        create an empty graph mapping airports to destination min-heaps
        create an empty route

        for each source and destination ticket:
            add the destination to the source airport's min-heap

        visit(current_airport):
            while the current airport has unused destination tickets:
                remove the lexicographically smallest destination
                visit that destination
            append the current airport to the route

        visit JFK
        reverse and return the route

Time complexity: O(E log E)
Space complexity: O(E)
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """Return the smallest valid itinerary that uses every ticket once."""
        graph: defaultdict[str, list[str]] = defaultdict(list)

        for source, destination in tickets:
            heappush(graph[source], destination)

        route: list[str] = []

        def visit(current_airport: str) -> None:
            while graph[current_airport]:
                next_airport = heappop(graph[current_airport])
                visit(next_airport)

            route.append(current_airport)

        visit("JFK")
        route.reverse()
        return route


def test_example_1() -> None:
    """Run the first worked example."""
    tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
    expected = ["JFK", "BUF", "HOU", "SEA"]
    assert Solution().findItinerary(tickets) == expected


def test_example_2() -> None:
    """Run the lexicographical-order worked example."""
    tickets = [
        ["HOU", "JFK"],
        ["SEA", "JFK"],
        ["JFK", "SEA"],
        ["JFK", "HOU"],
    ]
    expected = ["JFK", "HOU", "JFK", "SEA", "JFK"]
    assert Solution().findItinerary(tickets) == expected


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
