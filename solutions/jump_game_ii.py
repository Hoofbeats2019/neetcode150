"""Jump Game II.

Created: 2 September 2026
Created by: Yanlong Su

You are given an integer array ``nums`` where each element ``nums[i]``
indicates the maximum jump length to the right from index ``i``.

Starting at index 0, return the minimum number of jumps required to reach the
last index. A valid sequence of jumps is always possible.

Example 1:
    Input: nums = [2, 4, 1, 1, 1, 1]
    Output: 2
    Explanation: Jump from index 0 to index 1, then from index 1 to the last
        index.

Example 2:
    Input: nums = [2, 1, 2, 1, 0]
    Output: 2

Constraints:
    1 <= len(nums) <= 1,000
    0 <= nums[i] <= 100

Pseudocode:
    minJumps(nums):
        create an empty memo

        dfs(index):
            if index is the last index, return 0
            if index is in memo, return its stored result

            min_steps = len(nums) - index
            for jump_length from 1 through nums[index]:
                next_index = index + jump_length
                if next_index is within nums:
                    steps_from_next = dfs(next_index)
                    min_steps = min(min_steps, steps_from_next + 1)

            store min_steps in memo for index
            return min_steps

        return dfs(0)

Time complexity: O(n²)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """Return the minimum jumps needed to reach the last index."""
        memo: dict[int, int] = {}
        last_index = len(nums) - 1

        def dfs(index: int) -> int:
            if index == last_index:
                return 0

            if index in memo:
                return memo[index]

            min_steps = len(nums) - index

            for jump_length in range(1, nums[index] + 1):
                next_index = index + jump_length

                if next_index <= last_index:
                    steps_from_next = dfs(next_index)
                    min_steps = min(min_steps, steps_from_next + 1)

            memo[index] = min_steps
            return min_steps

        return dfs(0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().jump([2, 4, 1, 1, 1, 1]) == 2


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().jump([2, 1, 2, 1, 0]) == 2


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
