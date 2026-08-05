"""Median of Two Sorted Arrays.

Created: 5 August 2026
Created by: Yanlong Su

Given two integer arrays sorted in ascending order, return the median value
among all their elements in O(log(m + n)) time.

Example 1:
    Input: nums1 = [1, 2], nums2 = [3]
    Output: 2.0

Example 2:
    Input: nums1 = [1, 3], nums2 = [2, 4]
    Output: 2.5

Executable examples:
    >>> solution = Solution()
    >>> solution.findMedianSortedArrays([1, 2], [3])
    2.0
    >>> solution.findMedianSortedArrays([1, 3], [2, 4])
    2.5

Constraints:
    0 <= nums1.length, nums2.length <= 1000
    1 <= nums1.length + nums2.length <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # Binary search the shorter array to keep the search O(log(min(m, n))).
        shorter, longer = nums1, nums2
        if len(shorter) > len(longer):
            shorter, longer = longer, shorter

        shorter_length = len(shorter)
        longer_length = len(longer)

        # The left half contains one extra value when the total length is odd.
        left_size = (shorter_length + longer_length + 1) // 2

        # A partition is a position between values, so it can range from
        # 0 (nothing on the left) to len(shorter) (everything on the left).
        left = 0
        right = shorter_length

        while left <= right:
            # Choose how many values from each array belong in the left half.
            shorter_partition = (left + right) // 2
            longer_partition = left_size - shorter_partition

            # Infinity handles partitions at the beginning or end of an array.
            # This lets us compare boundaries without separate edge-case logic.
            shorter_left = (
                shorter[shorter_partition - 1]
                if shorter_partition > 0
                else float("-inf")
            )
            shorter_right = (
                shorter[shorter_partition]
                if shorter_partition < shorter_length
                else float("inf")
            )
            longer_left = (
                longer[longer_partition - 1]
                if longer_partition > 0
                else float("-inf")
            )
            longer_right = (
                longer[longer_partition]
                if longer_partition < longer_length
                else float("inf")
            )

            # The partition is correct when every value in the combined left
            # half is less than or equal to every value in the combined right.
            if shorter_left <= longer_right and longer_left <= shorter_right:
                left_maximum = max(shorter_left, longer_left)

                # With an odd number of values, the extra left value is median.
                if (shorter_length + longer_length) % 2 == 1:
                    return float(left_maximum)

                # With an even number of values, average the two middle values.
                right_minimum = min(shorter_right, longer_right)
                return (left_maximum + right_minimum) / 2.0

            # Too many values from the shorter array are on the left.
            if shorter_left > longer_right:
                right = shorter_partition - 1
            else:
                # Too few values from the shorter array are on the left.
                left = shorter_partition + 1

        raise ValueError("Input arrays must be sorted in ascending order")


def test_example_1() -> None:
    solution = Solution()
    actual = solution.findMedianSortedArrays([1, 2], [3])
    expected = 2.0
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.findMedianSortedArrays([1, 3], [2, 4])
    expected = 2.5
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
