"""Unit tests for Course Schedule II."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.course_schedule_ii import Solution


class TestCourseScheduleII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertValidOrder(
        self,
        num_courses: int,
        prerequisites: list[list[int]],
        order: list[int],
    ) -> None:
        self.assertEqual(len(order), num_courses)
        self.assertEqual(set(order), set(range(num_courses)))

        positions = {
            course: index for index, course in enumerate(order)
        }
        for course, prerequisite in prerequisites:
            self.assertLess(positions[prerequisite], positions[course])

    def test_one_prerequisite(self) -> None:
        self.assertEqual(self.solution.findOrder(2, [[1, 0]]), [0, 1])

    def test_multiple_valid_orderings(self) -> None:
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        order = self.solution.findOrder(4, prerequisites)
        self.assertValidOrder(4, prerequisites, order)

    def test_mutual_prerequisites_have_no_ordering(self) -> None:
        prerequisites = [[1, 0], [0, 1]]
        self.assertEqual(self.solution.findOrder(2, prerequisites), [])

    def test_single_course_without_prerequisites(self) -> None:
        self.assertEqual(self.solution.findOrder(1, []), [0])

    def test_disconnected_courses_are_all_included(self) -> None:
        prerequisites = [[1, 0], [3, 2]]
        order = self.solution.findOrder(5, prerequisites)
        self.assertValidOrder(5, prerequisites, order)

    def test_longer_cycle_has_no_ordering(self) -> None:
        prerequisites = [[1, 0], [2, 1], [0, 2]]
        self.assertEqual(self.solution.findOrder(3, prerequisites), [])

    def test_course_cannot_require_itself(self) -> None:
        self.assertEqual(self.solution.findOrder(1, [[0, 0]]), [])

    def test_chain_at_constraint_limit(self) -> None:
        prerequisites = [
            [course, course - 1] for course in range(1, 2000)
        ]
        expected = list(range(2000))
        self.assertEqual(
            self.solution.findOrder(2000, prerequisites),
            expected,
        )


if __name__ == "__main__":
    unittest.main()
