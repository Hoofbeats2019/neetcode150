"""Merge Intervals.

Created: 2 September 2026
Created by: Yanlong Su

Given a list of intervals where ``intervals[i] = [start_i, end_i]``, merge
every overlapping interval and return the resulting non-overlapping intervals.
Intervals that share an endpoint overlap.

Example 1:
    Input: intervals = [[1, 3], [1, 5], [6, 7]]
    Output: [[1, 5], [6, 7]]

Example 2:
    Input: intervals = [[1, 2], [2, 3]]
    Output: [[1, 3]]

Constraints:
    1 <= len(intervals) <= 1,000
    len(intervals[i]) == 2
    0 <= start_i <= end_i <= 1,000

Approach:
    Sort intervals by their start time. Keep the current merged interval while
    scanning the remaining intervals. If the next interval starts at or before
    the current end, extend the current end when needed. Otherwise, append the
    current interval and begin a new one.

Time complexity: O(n log n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge overlapping intervals into a non-overlapping result."""
        intervals.sort(key=lambda interval: interval[0])
        merged: List[List[int]] = [intervals[0]]

        for start, end in intervals[1:]:
            current_end = merged[-1][1]

            if start <= current_end:
                merged[-1][1] = max(current_end, end)
            else:
                merged.append([start, end])

        return merged


def test_example_1() -> None:
    """Run the first worked example."""
    expected = [[1, 5], [6, 7]]
    actual = Solution().merge([[1, 3], [1, 5], [6, 7]])
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = [[1, 3]]
    actual = Solution().merge([[1, 2], [2, 3]])
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
