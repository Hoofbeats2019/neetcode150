"""Longest Increasing Subsequence.

Created: 30 August 2026
Created by: Yanlong Su

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence can be derived from the given sequence by deleting some or no
elements without changing the relative order of the remaining elements.

Example 1:
    Input: nums = [9, 1, 4, 2, 3, 3, 7]
    Output: 4
    Explanation: The longest increasing subsequence is [1, 2, 3, 7].

Example 2:
    Input: nums = [0, 3, 1, 3, 2, 3]
    Output: 4
    Explanation: The longest increasing subsequence is [0, 1, 2, 3].

Constraints:
    1 <= len(nums) <= 1000
    -1000 <= nums[i] <= 1000

Pseudocode:
    lengthOfLIS(nums):
        create an empty tails list

        for each number in nums:
            set low to 0 and high to the length of tails

            while low is less than high:
                set middle to the midpoint of low and high

                if tails[middle] is smaller than number:
                    move low to middle + 1
                otherwise:
                    move high to middle

            if low is at the end of tails:
                append number
            otherwise:
                replace tails[low] with number

        return the length of tails

Time complexity: O(n log n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Return the length of the longest strictly increasing subsequence."""
        tails: List[int] = []

        for number in nums:
            low = 0
            high = len(tails)

            while low < high:
                middle = (low + high) // 2

                if tails[middle] < number:
                    low = middle + 1
                else:
                    high = middle

            if low == len(tails):
                tails.append(number)
            else:
                tails[low] = number

        return len(tails)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().lengthOfLIS([9, 1, 4, 2, 3, 3, 7]) == 4


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().lengthOfLIS([0, 3, 1, 3, 2, 3]) == 4


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
