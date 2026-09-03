"""Unit tests for Meeting Rooms II."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.meeting_rooms_ii import Interval, Solution


class TestMeetingRoomsII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        actual = self.solution.minMeetingRooms(
            [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
        )
        self.assertEqual(actual, 2)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.minMeetingRooms([Interval(4, 9)]), 1)

    def test_empty_schedule(self) -> None:
        self.assertEqual(self.solution.minMeetingRooms([]), 0)

    def test_touching_meetings_share_a_room(self) -> None:
        actual = self.solution.minMeetingRooms([Interval(0, 8), Interval(8, 10)])
        self.assertEqual(actual, 1)

    def test_three_simultaneous_meetings_need_three_rooms(self) -> None:
        actual = self.solution.minMeetingRooms(
            [Interval(0, 10), Interval(1, 9), Interval(2, 8)]
        )
        self.assertEqual(actual, 3)

    def test_unsorted_meetings_reuse_finished_rooms(self) -> None:
        actual = self.solution.minMeetingRooms(
            [Interval(15, 20), Interval(0, 40), Interval(5, 10)]
        )
        self.assertEqual(actual, 2)


if __name__ == "__main__":
    unittest.main()
