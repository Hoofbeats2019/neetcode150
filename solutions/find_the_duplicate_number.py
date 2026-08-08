"""Find the Duplicate Number.

Created: 8 August 2026
Created by: Yanlong Su

Given an array containing n + 1 integers where every integer is in the range
[1, n], return the one repeated integer. Every other integer appears at most
once.

The input array must not be modified, and the solution must use O(1) extra
space.

Example 1:
    Input: nums = [1, 2, 3, 2, 2]
    Output: 2

Example 2:
    Input: nums = [1, 2, 3, 4, 4]
    Output: 4

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


def test_examples() -> None:
    solution = Solution()

    assert solution.findDuplicate([1, 2, 3, 2, 2]) == 2
    assert solution.findDuplicate([1, 2, 3, 4, 4]) == 4


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
