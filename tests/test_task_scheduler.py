"""Unit tests for Task Scheduler.

Test pseudocode:
    for each worked example:
        schedule every task with the required cooldown
        verify the minimum number of CPU cycles

    for edge cases:
        verify no cooldown needs no idle cycles
        verify a single task takes one cycle
        verify distinct tasks do not require idle cycles
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.task_scheduler import Solution


class TestTaskScheduler(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(
            self.solution.leastInterval(["X", "X", "Y", "Y"], 2), 5
        )

    def test_second_example(self) -> None:
        self.assertEqual(
            self.solution.leastInterval(["A", "A", "A", "B", "C"], 3), 9
        )

    def test_no_cooldown(self) -> None:
        self.assertEqual(self.solution.leastInterval(["A", "A", "B"], 0), 3)

    def test_single_task(self) -> None:
        self.assertEqual(self.solution.leastInterval(["Z"], 100), 1)

    def test_all_tasks_are_distinct(self) -> None:
        self.assertEqual(self.solution.leastInterval(["A", "B", "C"], 2), 3)


if __name__ == "__main__":
    unittest.main()
