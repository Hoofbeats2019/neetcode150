"""Climbing Stairs.

Created: 23 August 2026
Created by: Yanlong Su

You are given an integer ``n`` representing the number of steps needed to
reach the top of a staircase. You may climb either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:
    Input: n = 2
    Output: 2
    Explanation: The distinct ways are 1 + 1 and 2.

Example 2:
    Input: n = 3
    Output: 3
    Explanation: The distinct ways are 1 + 1 + 1, 1 + 2, and 2 + 1.

Constraints:
    1 <= n <= 45

Pseudocode:
    climbStairs(n):
        create an empty memo

        ways(steps):
            if steps is 1, return 1
            if steps is 2, return 2
            if steps is already in memo, return its stored result

            store ways(steps - 1) + ways(steps - 2) in memo
            return the stored result

        return ways(n)

Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """Return the number of distinct ways to climb ``n`` steps."""
        memo: dict[int, int] = {}

        def ways(steps: int) -> int:
            if steps == 1:
                return 1

            if steps == 2:
                return 2

            if steps in memo:
                return memo[steps]

            memo[steps] = ways(steps - 1) + ways(steps - 2)

            return memo[steps]

        return ways(n)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().climbStairs(2) == 2


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().climbStairs(3) == 3


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
