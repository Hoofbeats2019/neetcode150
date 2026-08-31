"""Target Sum.

Created: 31 August 2026
Created by: Yanlong Su

You are given an array of integers ``nums`` and an integer ``target``.

For every number in ``nums``, choose either a plus or minus sign. Return the
number of distinct signed expressions whose total equals ``target``.

Example 1:
    Input: nums = [2, 2, 2], target = 2
    Output: 3
    Explanation: The expressions ``+2 +2 -2``, ``+2 -2 +2``, and
        ``-2 +2 +2`` each total 2.

Constraints:
    1 <= len(nums) <= 20
    0 <= nums[i] <= 1000
    -1000 <= target <= 1000

Pseudocode:
    findTargetSumWays(nums, target):
        create an empty memo

        dp(index, remainingTarget):
            if index reaches the end of nums:
                return 1 when remainingTarget is 0, otherwise 0
            if (index, remainingTarget) is in memo:
                return its stored result

            add current number:
                solve dp(index + 1, remainingTarget - nums[index])
            subtract current number:
                solve dp(index + 1, remainingTarget + nums[index])

            store and return the sum of both choices

        return dp(0, target)

Time complexity: O(n * sum(nums))
Space complexity: O(n * sum(nums))
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Return the number of signed expressions that equal ``target``."""
        memo: dict[tuple[int, int], int] = {}

        def dp(index: int, remaining_target: int) -> int:
            if index == len(nums):
                return 1 if remaining_target == 0 else 0

            state = (index, remaining_target)

            if state in memo:
                return memo[state]

            add_current = dp(index + 1, remaining_target - nums[index])
            subtract_current = dp(
                index + 1,
                remaining_target + nums[index],
            )

            memo[state] = add_current + subtract_current
            return memo[state]

        return dp(0, target)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().findTargetSumWays([2, 2, 2], 2) == 3


if __name__ == "__main__":
    test_example_1()
    print("The example test passed.")
