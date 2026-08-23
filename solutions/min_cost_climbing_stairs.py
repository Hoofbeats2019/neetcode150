"""Min Cost Climbing Stairs.

Created: 23 August 2026
Created by: Yanlong Su

You are given an integer array ``cost`` where ``cost[i]`` is the cost of
taking a step from the ``i``th floor of a staircase. After paying the cost,
you may step to either the ``(i + 1)``th floor or the ``(i + 2)``th floor.

You may start from step 0 or step 1. Return the minimum cost required to reach
the top of the staircase, which is just beyond the final indexed step.

Example 1:
    Input: cost = [1, 2, 3]
    Output: 2
    Explanation: Start at index 1, pay a cost of 2, and take two steps to
    reach the top.

Example 2:
    Input: cost = [1, 2, 1, 2, 1, 1, 1]
    Output: 4
    Explanation: Pay the costs at indices 0, 2, 4, and 6 before reaching the
    top.

Constraints:
    2 <= len(cost) <= 100
    0 <= cost[i] <= 100

Pseudocode:
    minCostClimbingStairs(cost):
        create an empty memo

        solve(n):
            if n is 0 or 1, return 0
            if n is already in memo, return its stored result

            one_step = solve(n - 1) + cost[n - 1]
            two_steps = solve(n - 2) + cost[n - 2]
            store the smaller cost in memo for n
            return the stored result

        return solve(length of cost)

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Return the minimum cost required to reach the top."""
        memo: dict[int, int] = {}

        def solve(floor: int) -> int:
            if floor == 0 or floor == 1:
                return 0

            if floor in memo:
                return memo[floor]

            one_step_cost = solve(floor - 1) + cost[floor - 1]
            two_step_cost = solve(floor - 2) + cost[floor - 2]
            memo[floor] = min(one_step_cost, two_step_cost)

            return memo[floor]

        return solve(len(cost))


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().minCostClimbingStairs([1, 2, 3]) == 2


def test_example_2() -> None:
    """Run the second worked example."""
    cost = [1, 2, 1, 2, 1, 1, 1]
    assert Solution().minCostClimbingStairs(cost) == 4


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
