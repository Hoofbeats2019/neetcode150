"""Gas Station.

Created: 2 September 2026
Created by: Yanlong Su

There are ``n`` gas stations along a circular route. ``gas[i]`` is the amount
of gas available at station ``i``, and ``cost[i]`` is the gas needed to travel
from station ``i`` to station ``(i + 1)``. The last station connects to the
first station.

The car starts with an empty tank and has unlimited capacity. Return the index
of a station from which the car can complete one clockwise circuit, or ``-1``
when no such starting station exists. At most one valid answer exists.

Example 1:
    Input: gas = [1, 2, 3, 4], cost = [2, 2, 4, 1]
    Output: 3

Example 2:
    Input: gas = [1, 2, 3], cost = [2, 3, 2]
    Output: -1

Constraints:
    1 <= len(gas) == len(cost) <= 100,000
    0 <= gas[i], cost[i] <= 1,000

Approach:
    Scan the stations once while tracking the total fuel balance and the fuel
    balance since the current candidate start. When that local balance becomes
    negative, every start in the failed segment is impossible, so the next
    station becomes the new candidate. A negative total balance means no
    complete circuit exists.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Return a valid starting-station index, or -1 when none exists."""
        total_balance = 0
        current_balance = 0
        start = 0

        for index, (station_gas, travel_cost) in enumerate(zip(gas, cost)):
            balance = station_gas - travel_cost
            total_balance += balance
            current_balance += balance

            if current_balance < 0:
                start = index + 1
                current_balance = 0

        return start if total_balance >= 0 else -1


def test_example_1() -> None:
    """Run the first worked example."""
    expected = 3
    actual = Solution().canCompleteCircuit([1, 2, 3, 4], [2, 2, 4, 1])
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = -1
    actual = Solution().canCompleteCircuit([1, 2, 3], [2, 3, 2])
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
