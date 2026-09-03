"""Meeting Rooms II.

Created: 3 September 2026
Created by: Yanlong Su

Given meeting interval objects with ``start`` and ``end`` attributes, return
the minimum number of rooms needed to schedule every meeting without a
conflict. Meetings that share an endpoint do not conflict.

Example 1:
    Input: intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    Output: 2
    Explanation: One room holds [0, 40]; another holds [5, 10] and [15, 20].

Example 2:
    Input: intervals = [Interval(4, 9)]
    Output: 1

Constraints:
    0 <= len(intervals) <= 100,000
    0 <= start_i < end_i <= 1,000,000

Approach:
    Sort meetings by start time. Store the end times of active meetings in a
    min-heap, so its first value is the room that becomes available first.
    Before assigning each meeting, remove every room whose meeting has ended.
    Add the current end time and record the largest number of active rooms.

Time complexity: O(n log n)
Space complexity: O(n)
"""

from heapq import heappop, heappush
from typing import List


class Interval:
    """A meeting interval with a start time and an end time."""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """Return the minimum number of rooms required for all meetings."""
        intervals.sort(key=lambda interval: interval.start)
        active_end_times: list[int] = []
        maximum_rooms = 0

        for interval in intervals:
            while active_end_times and active_end_times[0] <= interval.start:
                heappop(active_end_times)

            heappush(active_end_times, interval.end)
            maximum_rooms = max(maximum_rooms, len(active_end_times))

        return maximum_rooms


def test_example_1() -> None:
    """Run the first worked example."""
    expected = 2
    actual = Solution().minMeetingRooms(
        [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    )
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = 1
    actual = Solution().minMeetingRooms([Interval(4, 9)])
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
