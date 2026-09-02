"""Unit tests for Partition Labels."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.partition_labels import Solution


class TestPartitionLabels(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(
            self.solution.partitionLabels("xyxxyzbzbbisl"),
            [5, 5, 1, 1, 1],
        )

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.partitionLabels("abcabc"), [6])

    def test_all_distinct_characters(self) -> None:
        self.assertEqual(self.solution.partitionLabels("abc"), [1, 1, 1])

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.partitionLabels("a"), [1])


if __name__ == "__main__":
    unittest.main()
