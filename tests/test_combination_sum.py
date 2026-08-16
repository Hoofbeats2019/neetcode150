"""Unit tests for Combination Sum.

Test pseudocode:
    for each worked example:
        request all combinations that sum to the target
        normalize the number ordering within each combination
        normalize the combination ordering within the result
        verify the expected combinations are returned exactly once

    for an edge case:
        verify a value equal to the target forms one combination
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.combination_sum import Solution


class TestCombinationSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertCombinationsEqual(
        self,
        actual: list[list[int]],
        expected: list[list[int]],
    ) -> None:
        normalized_actual = sorted(
            tuple(sorted(combination)) for combination in actual
        )
        normalized_expected = sorted(
            tuple(sorted(combination)) for combination in expected
        )
        self.assertEqual(normalized_actual, normalized_expected)

    def test_repeated_value_and_direct_match(self) -> None:
        actual = self.solution.combinationSum([2, 5, 6, 9], 9)
        self.assertCombinationsEqual(actual, [[2, 2, 5], [9]])

    def test_multiple_combinations(self) -> None:
        actual = self.solution.combinationSum([3, 4, 5], 16)
        expected = [
            [3, 3, 3, 3, 4],
            [3, 3, 5, 5],
            [4, 4, 4, 4],
            [3, 4, 4, 5],
        ]
        self.assertCombinationsEqual(actual, expected)

    def test_no_combination(self) -> None:
        actual = self.solution.combinationSum([3], 5)
        self.assertEqual(actual, [])

    def test_single_value_equal_to_target(self) -> None:
        actual = self.solution.combinationSum([2, 3], 2)
        self.assertCombinationsEqual(actual, [[2]])


if __name__ == "__main__":
    unittest.main()
