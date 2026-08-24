"""House Robber II.

Created: 24 August 2026
Created by: Yanlong Su

You are given an integer array ``nums`` where ``nums[i]`` represents the
amount of money in the ``i``th house. The houses are arranged in a circle, so
the first and last houses are neighbors. Robbing two adjacent houses alerts
the police.

Return the maximum amount of money that can be robbed without alerting the
police.

Example 1:
    Input: nums = [3, 4, 3]
    Output: 4
    Explanation: Houses 0 and 2 are adjacent, so the best choice is house 1.

Example 2:
    Input: nums = [2, 9, 8, 3, 6]
    Output: 15
    Explanation: Rob houses 1 and 4 for 9 + 6 = 15.

Constraints:
    1 <= len(nums) <= 100
    0 <= nums[i] <= 200

Pseudocode:
    rob(nums):
        if there is one house, return its money
        create an empty memo

        solve(start, index):
            if index is before start, return 0
            if (start, index) is already in memo, return its stored result

            skip_current = solve(start, index - 1)
            rob_current = nums[index] + solve(start, index - 2)
            store the larger result in memo for (start, index)
            return the stored result

        case_1 = solve(0, n - 2)
        case_2 = solve(1, n - 1)
        return the larger result

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Return the maximum money obtainable from circular houses."""
        if len(nums) == 1:
            return nums[0]

        memo: dict[tuple[int, int], int] = {}

        def solve(start: int, index: int) -> int:
            if index < start:
                return 0

            key = (start, index)
            if key in memo:
                return memo[key]

            skip_current = solve(start, index - 1)
            rob_current = nums[index] + solve(start, index - 2)
            memo[key] = max(skip_current, rob_current)

            return memo[key]

        exclude_last = solve(0, len(nums) - 2)
        exclude_first = solve(1, len(nums) - 1)
        return max(exclude_last, exclude_first)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().rob([3, 4, 3]) == 4


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().rob([2, 9, 8, 3, 6]) == 15


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
