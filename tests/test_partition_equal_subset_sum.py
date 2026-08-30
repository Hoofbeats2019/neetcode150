"""Unit tests for Partition Equal Subset Sum."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.partition_equal_subset_sum import Solution


class TestPartitionEqualSubsetSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(self.solution.canPartition([1, 2, 3, 4]))

    def test_second_worked_example(self) -> None:
        self.assertFalse(self.solution.canPartition([1, 2, 3, 4, 5]))

    def test_duplicate_values_are_separate_elements(self) -> None:
        self.assertTrue(self.solution.canPartition([1, 1]))

    def test_single_element_cannot_be_partitioned_equally(self) -> None:
        self.assertFalse(self.solution.canPartition([1]))

    def test_odd_total_cannot_be_partitioned_equally(self) -> None:
        self.assertFalse(self.solution.canPartition([1, 2, 4]))

    def test_even_total_without_target_subset_returns_false(self) -> None:
        self.assertFalse(self.solution.canPartition([2, 2, 3, 5]))

    def test_maximum_length_with_equal_values(self) -> None:
        self.assertTrue(self.solution.canPartition([50] * 100))


if __name__ == "__main__":
    unittest.main()
