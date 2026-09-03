"""Meeting Rooms.

Created: 3 September 2026
Created by: Yanlong Su

Given meeting interval objects with ``start`` and ``end`` attributes, determine
whether one person can attend every meeting without a time conflict. The
intervals may be in any order. Meetings that share an endpoint do not conflict.

Example 1:
    Input: intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    Output: False
    Explanation: [0, 30] conflicts with both [5, 10] and [15, 20].

Example 2:
    Input: intervals = [Interval(5, 8), Interval(9, 15)]
    Output: True

Constraints:
    0 <= len(intervals) <= 500
    0 <= start_i < end_i <= 1,000,000

Approach:
    Sort the intervals by start time. Compare each meeting's start with the
    previous meeting's end. If a start is earlier than that end, the meetings
    conflict; otherwise, continue until every meeting has been checked.

Time complexity: O(n log n)
Space complexity: O(1) auxiliary space, excluding the sorting implementation.
"""

from typing import List


class Interval:
    """A meeting interval with a start time and an end time."""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """Return whether all meetings can be attended without conflicts."""
        intervals.sort(key=lambda interval: interval.start)

        for index in range(1, len(intervals)):
            start = intervals[index].start
            previous_end = intervals[index - 1].end

            if start < previous_end:
                return False

        return True


def test_example_1() -> None:
    """Run the first worked example."""
    expected = False
    actual = Solution().canAttendMeetings(
        [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    )
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = True
    actual = Solution().canAttendMeetings([Interval(5, 8), Interval(9, 15)])
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
