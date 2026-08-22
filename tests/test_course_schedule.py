"""Unit tests for Course Schedule."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.course_schedule import Solution


class TestCourseSchedule(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_prerequisite_can_be_completed(self) -> None:
        self.assertTrue(self.solution.canFinish(2, [[0, 1]]))

    def test_mutual_prerequisites_cannot_be_completed(self) -> None:
        self.assertFalse(self.solution.canFinish(2, [[0, 1], [1, 0]]))

    def test_single_course_without_prerequisites(self) -> None:
        self.assertTrue(self.solution.canFinish(1, []))

    def test_separate_prerequisite_relationships(self) -> None:
        prerequisites = [[1, 0], [3, 2]]
        self.assertTrue(self.solution.canFinish(4, prerequisites))

    def test_paths_may_merge_without_forming_a_cycle(self) -> None:
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        self.assertTrue(self.solution.canFinish(4, prerequisites))

    def test_longer_cycle_cannot_be_completed(self) -> None:
        prerequisites = [[1, 0], [2, 1], [0, 2]]
        self.assertFalse(self.solution.canFinish(3, prerequisites))

    def test_course_cannot_require_itself(self) -> None:
        self.assertFalse(self.solution.canFinish(1, [[0, 0]]))

    def test_chain_at_constraint_limit(self) -> None:
        prerequisites = [
            [course, course - 1] for course in range(1, 1000)
        ]
        self.assertTrue(self.solution.canFinish(1000, prerequisites))


if __name__ == "__main__":
    unittest.main()
