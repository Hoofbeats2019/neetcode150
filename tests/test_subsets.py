"""Unit tests for Subsets.

Test pseudocode:
    for each worked example:
        request every subset
        normalize the subset and result ordering
        verify the expected subsets are returned exactly once

    for an edge case:
        verify negative and positive integers are handled
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.subsets import Solution


class TestSubsets(unittest.TestCase):
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

    def test_three_integers(self) -> None:
        actual = self.solution.subsets([1, 2, 3])
        expected = [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
        self.assertSubsetsEqual(actual, expected)

    def test_single_integer(self) -> None:
        actual = self.solution.subsets([7])
        self.assertSubsetsEqual(actual, [[], [7]])

    def test_negative_and_positive_integers(self) -> None:
        actual = self.solution.subsets([-1, 2])
        self.assertSubsetsEqual(actual, [[], [-1], [2], [-1, 2]])


if __name__ == "__main__":
    unittest.main()
