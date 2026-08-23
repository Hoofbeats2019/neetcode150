"""Network Delay Time.

Created: 23 August 2026
Created by: Yanlong Su

You are given a network of ``n`` directed nodes labeled from ``1`` to ``n``.
Each entry ``[u, v, t]`` in ``times`` describes a directed edge from node
``u`` to node ``v`` that takes ``t`` units of time to travel.

A signal is sent from node ``k``. Return the minimum time required for every
node to receive the signal. Return ``-1`` if at least one node cannot receive
the signal.

Example 1:
    Input:
        times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
        n = 4
        k = 1
    Output: 3

Example 2:
    Input:
        times = [[1, 2, 1], [2, 3, 1]]
        n = 3
        k = 2
    Output: -1

Constraints:
    1 <= k <= n <= 100
    1 <= len(times) <= 1000
    len(times[i]) == 3
    1 <= times[i][0], times[i][1] <= n
    times[i][2] >= 0

Pseudocode:
    networkDelayTime(times, n, k):
        create an adjacency matrix filled with infinity
        for each directed edge:
            store its travel time in the matrix

        create a distances array filled with infinity
        set the distance to k to zero
        mark every node as unvisited

        repeat n times:
            find the unvisited node with the smallest distance
            stop if no reachable unvisited node remains
            mark that node as visited

            for each of its outgoing neighbors:
                calculate the cost of traveling through the current node
                keep the smaller cost for that neighbor

        return -1 if any node's distance is infinity
        otherwise return the maximum shortest-path distance

Time complexity: O(n^2 + E)
Space complexity: O(n^2)
"""

from typing import List


class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int,
    ) -> int:
        """Return when all nodes receive the signal, or -1 if impossible."""
        infinity = float("inf")
        graph = [
            [infinity] * (n + 1)
            for _ in range(n + 1)
        ]

        for source, target, travel_time in times:
            graph[source][target] = min(
                graph[source][target],
                travel_time,
            )

        distances = [infinity] * (n + 1)
        distances[k] = 0
        visited = [False] * (n + 1)

        for _ in range(n):
            current_node = -1

            for node in range(1, n + 1):
                if visited[node]:
                    continue

                if (
                    current_node == -1
                    or distances[node] < distances[current_node]
                ):
                    current_node = node

            if (
                current_node == -1
                or distances[current_node] == infinity
            ):
                break

            visited[current_node] = True

            for neighbor in range(1, n + 1):
                if graph[current_node][neighbor] == infinity:
                    continue

                new_cost = (
                    distances[current_node]
                    + graph[current_node][neighbor]
                )
                distances[neighbor] = min(
                    distances[neighbor],
                    new_cost,
                )

        maximum_delay = 0

        for node in range(1, n + 1):
            if distances[node] == infinity:
                return -1

            maximum_delay = max(maximum_delay, distances[node])

        return maximum_delay


def test_example_1() -> None:
    """Run the first worked example."""
    times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
    assert Solution().networkDelayTime(times, 4, 1) == 3


def test_example_2() -> None:
    """Run the second worked example."""
    times = [[1, 2, 1], [2, 3, 1]]
    assert Solution().networkDelayTime(times, 3, 2) == -1


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
