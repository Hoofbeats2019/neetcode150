"""Binary Search.

Created: 2 August 2026
Created by: Yanlong Su

You are given an array of distinct integers ``nums``, sorted in ascending
order, and an integer ``target``.

Return the index of ``target`` if it exists in ``nums``. Otherwise, return -1.

Example 1:
    Input: nums = [-1, 0, 2, 4, 6, 8], target = 4
    Output: 3

Example 2:
    Input: nums = [-1, 0, 2, 4, 6, 8], target = 3
    Output: -1

Executable examples:
    >>> solution = Solution()
    >>> solution.search([-1, 0, 2, 4, 6, 8], 4)
    3
    >>> solution.search([-1, 0, 2, 4, 6, 8], 3)
    -1

Constraints:
    1 <= nums.length <= 10000
    -10000 < nums[i], target < 10000
    All integers in nums are unique.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if target < nums[middle]:
                return binary_search(left, middle - 1)

            if target > nums[middle]:
                return binary_search(middle + 1, right)

            return -1

        return binary_search(0, len(nums) - 1)


def test_example_1() -> None:
    solution = Solution()
    actual = solution.search([-1, 0, 2, 4, 6, 8], 4)
    expected = 3
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.search([-1, 0, 2, 4, 6, 8], 3)
    expected = -1
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
