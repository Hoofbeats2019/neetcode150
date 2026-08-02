"""Find Minimum in Rotated Sorted Array.

Created: 2 August 2026
Created by: Yanlong Su

You are given an array of unique integers that was originally sorted in
ascending order and then rotated between 1 and n times.

Return the minimum element of the array in O(log n) time.

Example 1:
    Input: nums = [3, 4, 5, 6, 1, 2]
    Output: 1

Example 2:
    Input: nums = [4, 5, 0, 1, 2, 3]
    Output: 0

Example 3:
    Input: nums = [4, 5, 6, 7]
    Output: 4

Executable examples:
    >>> solution = Solution()
    >>> solution.findMin([3, 4, 5, 6, 1, 2])
    1
    >>> solution.findMin([4, 5, 0, 1, 2, 3])
    0
    >>> solution.findMin([4, 5, 6, 7])
    4

Constraints:
    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    All elements in nums are unique.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]


def test_example_1() -> None:
    solution = Solution()
    actual = solution.findMin([3, 4, 5, 6, 1, 2])
    expected = 1
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.findMin([4, 5, 0, 1, 2, 3])
    expected = 0
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_3() -> None:
    solution = Solution()
    actual = solution.findMin([4, 5, 6, 7])
    expected = 4
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
