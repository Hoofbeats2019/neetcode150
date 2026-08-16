"""Kth Largest Element in an Array.

Created: 15 August 2026
Created by: Yanlong Su

Given an unsorted array of integers ``nums`` and an integer ``k``, return the
kth largest element in the array.

The kth largest element is determined by sorted order, not by distinct values.

Follow-up:
    Can you solve it without sorting?

Example 1:
    Input: nums = [2, 3, 1, 5, 4], k = 2
    Output: 4

Example 2:
    Input: nums = [2, 3, 1, 1, 5, 5, 4], k = 3
    Output: 4

Constraints:
    ``nums`` contains at least one integer.
    1 <= k <= nums.length

Pseudocode:
    findKthLargest(nums, k):
        create an empty min-heap

        for each num in nums:
            push num into the min-heap

            if the size of the min-heap is greater than k:
                pop the smallest element from the min-heap

        return the top element of the min-heap
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the kth largest element in nums."""
        heap: list[int] = []

        for num in nums:
            heappush(heap, num)

            if len(heap) > k:
                heappop(heap)

        return heap[0]


def test_example_1() -> None:
    solution = Solution()
    actual = solution.findKthLargest([2, 3, 1, 5, 4], 2)
    expected = 4
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.findKthLargest([2, 3, 1, 1, 5, 5, 4], 3)
    expected = 4
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
