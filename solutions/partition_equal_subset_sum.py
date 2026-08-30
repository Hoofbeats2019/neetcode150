"""Partition Equal Subset Sum.

Created: 30 August 2026
Created by: Yanlong Su

You are given an array of positive integers ``nums``.

Return ``True`` if the array can be partitioned into two subsets whose sums
are equal. Otherwise, return ``False``.

Each occurrence in ``nums`` is a separate element, so duplicate values are
allowed and each occurrence may be selected at most once.

Example 1:
    Input: nums = [1, 2, 3, 4]
    Output: True
    Explanation: The array can be partitioned as ``[1, 4]`` and ``[2, 3]``.

Example 2:
    Input: nums = [1, 2, 3, 4, 5]
    Output: False

Constraints:
    1 <= len(nums) <= 100
    1 <= nums[i] <= 50

Pseudocode:
    canPartition(nums):
        calculate the total sum
        if the total sum is odd, return false

        set the target to half of the total sum
        create an empty memo

        search(index, remainingTarget):
            if remainingTarget is zero, return true
            if remainingTarget is negative, return false
            if index reaches the end of nums, return false
            if (index, remainingTarget) is in memo, return its result

            include the current number and search the smaller target
            skip the current number and search the unchanged target
            store whether either choice succeeds in memo
            return the stored result

        return search from index zero with the full target

Time complexity: O(n * target)
Space complexity: O(n * target)
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Return whether ``nums`` can be split into equal-sum subsets."""
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        memo: dict[tuple[int, int], bool] = {}

        def search(index: int, remaining_target: int) -> bool:
            if remaining_target == 0:
                return True

            if remaining_target < 0 or index == len(nums):
                return False

            state = (index, remaining_target)

            if state in memo:
                return memo[state]

            include_current = search(
                index + 1,
                remaining_target - nums[index],
            )
            skip_current = search(index + 1, remaining_target)

            memo[state] = include_current or skip_current
            return memo[state]

        return search(0, target)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().canPartition([1, 2, 3, 4]) is True


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().canPartition([1, 2, 3, 4, 5]) is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
