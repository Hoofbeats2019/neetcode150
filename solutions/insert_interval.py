"""Insert Interval.

Created: 2 September 2026
Created by: Yanlong Su

You are given a list of non-overlapping intervals ``intervals``, sorted by
starting time, and another interval ``newInterval``. Insert ``newInterval``
so the result remains sorted and has no overlaps. Intervals that overlap or
share an endpoint must be merged.

Example 1:
    Input: intervals = [[1, 3], [4, 6]], newInterval = [2, 5]
    Output: [[1, 6]]

Example 2:
    Input: intervals = [[1, 2], [3, 5], [9, 10]], newInterval = [6, 7]
    Output: [[1, 2], [3, 5], [6, 7], [9, 10]]

Constraints:
    0 <= len(intervals) <= 10,000
    len(newInterval) == len(intervals[i]) == 2
    0 <= start <= end <= 100,000

Approach:
    First copy every interval that ends before the new interval starts. Then
    merge each interval whose start is at or before the new interval's current
    end. Finally, append the merged interval and the untouched remaining
    intervals.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Insert ``newInterval`` and merge every overlapping interval."""
        result: List[List[int]] = []
        index = 0
        start, end = newInterval

        while index < len(intervals) and intervals[index][1] < start:
            result.append(intervals[index])
            index += 1

        while index < len(intervals) and intervals[index][0] <= end:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1

        result.append([start, end])

        while index < len(intervals):
            result.append(intervals[index])
            index += 1

        return result


def test_example_1() -> None:
    """Run the first worked example."""
    expected = [[1, 6]]
    actual = Solution().insert([[1, 3], [4, 6]], [2, 5])
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = [[1, 2], [3, 5], [6, 7], [9, 10]]
    actual = Solution().insert([[1, 2], [3, 5], [9, 10]], [6, 7])
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
