"""Search in Rotated Sorted Array.

Created: 5 August 2026
Created by: Yanlong Su

You are given an array of unique integers that was originally sorted in
ascending order and then rotated between 1 and n times, along with an integer
``target``.

Return the index of ``target`` if it exists in ``nums``. Otherwise, return -1.
The solution must run in O(log n) time.

Example 1:
    Input: nums = [3, 4, 5, 6, 1, 2], target = 1
    Output: 4

Example 2:
    Input: nums = [3, 5, 6, 0, 1, 2], target = 4
    Output: -1

Executable examples:
    >>> solution = Solution()
    >>> solution.search([3, 4, 5, 6, 1, 2], 1)
    4
    >>> solution.search([3, 5, 6, 0, 1, 2], 4)
    -1

Constraints:
    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -1000 <= target <= 1000
    All elements in nums are unique.
    nums is an ascending array that is possibly rotated.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotation_index = self._find_minimum_index(nums)

        if rotation_index == 0:
            return self._binary_search(nums, target, 0, len(nums) - 1)

        if target >= nums[0]:
            return self._binary_search(nums, target, 0, rotation_index - 1)

        return self._binary_search(
            nums, target, rotation_index, len(nums) - 1
        )

    def _find_minimum_index(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return left

    def _binary_search(
        self, nums: List[int], target: int, left: int, right: int
    ) -> int:
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


def test_example_1() -> None:
    solution = Solution()
    actual = solution.search([3, 4, 5, 6, 1, 2], 1)
    expected = 4
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.search([3, 5, 6, 0, 1, 2], 4)
    expected = -1
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
