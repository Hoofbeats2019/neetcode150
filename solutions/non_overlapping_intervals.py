"""Non-Overlapping Intervals.

Created: 3 September 2026
Created by: Yanlong Su

Given a list of intervals where ``intervals[i] = [start_i, end_i]``, return
the minimum number of intervals to remove so the remaining intervals do not
overlap. Intervals that share an endpoint do not overlap.

Example 1:
    Input: intervals = [[1, 2], [2, 4], [1, 4]]
    Output: 1
    Explanation: Remove [1, 4] so [1, 2] and [2, 4] remain.

Example 2:
    Input: intervals = [[1, 2], [2, 4]]
    Output: 0

Constraints:
    1 <= len(intervals) <= 100,000
    len(intervals[i]) == 2
    -50,000 <= start_i < end_i <= 50,000

Approach:
    Sort intervals by start time. Scan from left to right, comparing each
    start with the end of the previously kept interval. When the intervals
    overlap, remove one and retain the smaller end, because it leaves the most
    room for later intervals. When they do not overlap, keep the current end.

Time complexity: O(n log n)
Space complexity: O(1) auxiliary space, excluding the sorting implementation.
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Return the minimum number of intervals that must be removed."""
        intervals.sort(key=lambda interval: interval[0])
        removals = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= previous_end:
                previous_end = end
            else:
                removals += 1
                previous_end = min(previous_end, end)

        return removals


def test_example_1() -> None:
    """Run the first worked example."""
    expected = 1
    actual = Solution().eraseOverlapIntervals([[1, 2], [2, 4], [1, 4]])
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = 0
    actual = Solution().eraseOverlapIntervals([[1, 2], [2, 4]])
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
