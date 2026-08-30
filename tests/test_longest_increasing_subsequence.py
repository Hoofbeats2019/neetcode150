"""Unit tests for Longest Increasing Subsequence."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.longest_increasing_subsequence import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(
            self.solution.lengthOfLIS([9, 1, 4, 2, 3, 3, 7]),
            4,
        )

    def test_second_worked_example(self) -> None:
        self.assertEqual(
            self.solution.lengthOfLIS([0, 3, 1, 3, 2, 3]),
            4,
        )

    def test_single_element(self) -> None:
        self.assertEqual(self.solution.lengthOfLIS([5]), 1)

    def test_strictly_increasing_values(self) -> None:
        self.assertEqual(self.solution.lengthOfLIS([1, 2, 3, 4, 5]), 5)

    def test_strictly_decreasing_values(self) -> None:
        self.assertEqual(self.solution.lengthOfLIS([5, 4, 3, 2, 1]), 1)

    def test_equal_values_do_not_extend_the_subsequence(self) -> None:
        self.assertEqual(self.solution.lengthOfLIS([3, 3, 3, 3]), 1)

    def test_late_smaller_value_replaces_an_earlier_tail(self) -> None:
        self.assertEqual(self.solution.lengthOfLIS([9, 10, 5]), 2)

    def test_longer_sequence_discussed_in_worked_reasoning(self) -> None:
        self.assertEqual(
            self.solution.lengthOfLIS(
                [9, 1, 4, 2, 3, 3, 7, 9, 10, 6, 7, 8, 9, 10, 11, 12]
            ),
            10,
        )

    def test_negative_values(self) -> None:
        self.assertEqual(self.solution.lengthOfLIS([-5, -1, -3, 0, 2]), 4)


if __name__ == "__main__":
    unittest.main()
