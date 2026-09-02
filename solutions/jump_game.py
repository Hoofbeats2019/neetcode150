"""Jump Game.

Created: 2 September 2026
Created by: Yanlong Su

You are given an integer array ``nums`` where each element ``nums[i]``
indicates your maximum jump length at that position.

Return ``True`` if you can reach the last index starting from index 0, or
``False`` otherwise.

Example 1:
    Input: nums = [1, 2, 0, 1, 0]
    Output: True
    Explanation: Jump from index 0 to 1, then to 3, and finally to 4.

Example 2:
    Input: nums = [1, 2, 1, 0, 1]
    Output: False

Constraints:
    1 <= len(nums) <= 1,000
    0 <= nums[i] <= 1,000

Pseudocode:
    canJump(nums):
        create an empty memo

        dfs(index):
            if index is the last index, return True
            if index is in memo, return its stored result

            for jump_length from 1 through nums[index]:
                next_index = index + jump_length
                if next_index is within nums and dfs(next_index) is True:
                    store True in memo for index
                    return True

            store False in memo for index
            return False

        return dfs(0)

Time complexity: O(n²)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Return whether the last index is reachable from index 0."""
        memo: dict[int, bool] = {}
        last_index = len(nums) - 1

        def dfs(index: int) -> bool:
            if index == last_index:
                return True

            if index in memo:
                return memo[index]

            for jump_length in range(1, nums[index] + 1):
                next_index = index + jump_length
                if next_index <= last_index and dfs(next_index):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return dfs(0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().canJump([1, 2, 0, 1, 0]) is True


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().canJump([1, 2, 1, 0, 1]) is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
