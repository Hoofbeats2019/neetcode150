"""Unit tests for Meeting Rooms."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.meeting_rooms import Interval, Solution


class TestMeetingRooms(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertFalse(
            self.solution.canAttendMeetings(
                [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
            )
        )

    def test_second_worked_example(self) -> None:
        self.assertTrue(self.solution.canAttendMeetings([Interval(5, 8), Interval(9, 15)]))

    def test_touching_meetings_do_not_conflict(self) -> None:
        self.assertTrue(self.solution.canAttendMeetings([Interval(0, 8), Interval(8, 10)]))

    def test_unsorted_conflicting_meetings(self) -> None:
        self.assertFalse(
            self.solution.canAttendMeetings(
                [Interval(15, 20), Interval(5, 10), Interval(0, 30)]
            )
        )

    def test_empty_schedule(self) -> None:
        self.assertTrue(self.solution.canAttendMeetings([]))


if __name__ == "__main__":
    unittest.main()
