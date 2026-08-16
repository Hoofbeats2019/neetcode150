"""Unit tests for Subsets II.

Test pseudocode:
    for each worked example:
        request every unique subset
        normalize the subset and result ordering
        verify the expected subsets are returned exactly once

    for edge cases:
        verify separated duplicates do not create reordered duplicates
        verify distinct numbers still produce every subset
        verify the input list is not changed
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.subsets_ii import Solution


class TestSubsetsII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertSubsetsEqual(
        self,
        actual: list[list[int]],
        expected: list[list[int]],
    ) -> None:
        normalized_actual = sorted(tuple(sorted(subset)) for subset in actual)
        normalized_expected = sorted(
            tuple(sorted(subset)) for subset in expected
        )
        self.assertEqual(normalized_actual, normalized_expected)

    def test_separated_duplicate_values(self) -> None:
        actual = self.solution.subsetsWithDup([1, 2, 1])
        expected = [[], [1], [1, 2], [1, 1], [1, 2, 1], [2]]
        self.assertSubsetsEqual(actual, expected)

    def test_two_equal_values(self) -> None:
        actual = self.solution.subsetsWithDup([7, 7])
        self.assertSubsetsEqual(actual, [[], [7], [7, 7]])

    def test_negative_separated_duplicates(self) -> None:
        actual = self.solution.subsetsWithDup([-1, 2, -1])
        expected = [[], [-1], [-1, -1], [2], [-1, 2], [-1, -1, 2]]
        self.assertSubsetsEqual(actual, expected)

    def test_distinct_values(self) -> None:
        actual = self.solution.subsetsWithDup([1, 2, 3])
        expected = [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
        self.assertSubsetsEqual(actual, expected)

    def test_input_is_not_modified(self) -> None:
        nums = [3, 1, 3]
        original = nums.copy()

        self.solution.subsetsWithDup(nums)

        self.assertEqual(nums, original)


if __name__ == "__main__":
    unittest.main()
