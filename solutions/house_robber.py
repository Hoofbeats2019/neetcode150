"""House Robber.

Created: 23 August 2026
Created by: Yanlong Su

You are given an integer array ``nums`` where ``nums[i]`` represents the
amount of money in the ``i``th house. The houses are arranged in a straight
line, and robbing two adjacent houses alerts the police.

Return the maximum amount of money that can be robbed without alerting the
police.

Example 1:
    Input: nums = [1, 1, 3, 3]
    Output: 4
    Explanation: Rob houses 0 and 2 for 1 + 3 = 4.

Example 2:
    Input: nums = [2, 9, 8, 3, 6]
    Output: 16
    Explanation: Rob houses 0, 2, and 4 for 2 + 8 + 6 = 16.

Constraints:
    1 <= len(nums) <= 100
    0 <= nums[i] <= 100

Pseudocode:
    rob(nums):
        create an empty memo

        solve(index):
            if index is below 0, return 0
            if index is 0, return nums[0]
            if index is already in memo, return its stored result

            skip_last = solve(index - 1)
            rob_last = solve(index - 2) + nums[index]
            store the larger result in memo for index
            return the stored result

        return solve(last index)

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Return the maximum money obtainable from non-adjacent houses."""
        memo: dict[int, int] = {}

        def solve(index: int) -> int:
            if index < 0:
                return 0

            if index == 0:
                return nums[0]

            if index in memo:
                return memo[index]

            skip_last = solve(index - 1)
            rob_last = solve(index - 2) + nums[index]
            memo[index] = max(skip_last, rob_last)

            return memo[index]

        return solve(len(nums) - 1)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().rob([1, 1, 3, 3]) == 4


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().rob([2, 9, 8, 3, 6]) == 16


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
