"""Unit tests for Decode Ways."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.numDecodings("12"), 2)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.numDecodings("01"), 0)

    def test_grouping_example_from_description(self) -> None:
        self.assertEqual(self.solution.numDecodings("1012"), 2)

    def test_single_valid_digit(self) -> None:
        self.assertEqual(self.solution.numDecodings("7"), 1)

    def test_zero_cannot_decode_alone(self) -> None:
        self.assertEqual(self.solution.numDecodings("0"), 0)

    def test_zero_can_only_finish_ten_or_twenty(self) -> None:
        self.assertEqual(self.solution.numDecodings("10"), 1)
        self.assertEqual(self.solution.numDecodings("20"), 1)
        self.assertEqual(self.solution.numDecodings("30"), 0)

    def test_both_final_group_sizes_can_be_valid(self) -> None:
        self.assertEqual(self.solution.numDecodings("226"), 3)

    def test_consecutive_zeros_are_invalid(self) -> None:
        self.assertEqual(self.solution.numDecodings("100"), 0)

    def test_pair_above_twenty_six_is_not_used(self) -> None:
        self.assertEqual(self.solution.numDecodings("27"), 1)

    def test_maximum_length(self) -> None:
        self.assertEqual(self.solution.numDecodings("3" * 100), 1)


if __name__ == "__main__":
    unittest.main()
