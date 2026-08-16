"""Unit tests for Combination Sum II.

Test pseudocode:
    for each worked example:
        request all combinations that sum to the target
        normalize the number ordering within each combination
        normalize the combination ordering within the result
        verify the expected combinations are returned exactly once

    for edge cases:
        verify duplicate input values do not duplicate results
        verify one candidate cannot be reused
        verify an unreachable target returns no combinations
        verify the input list is not changed
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.combination_sum_ii import Solution


class TestCombinationSumII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertCombinationsEqual(
        self,
        actual: list[list[int]],
        expected: list[list[int]],
    ) -> None:
        # The problem permits any ordering, so compare normalized results.
        normalized_actual = sorted(
            tuple(sorted(combination)) for combination in actual
        )
        normalized_expected = sorted(
            tuple(sorted(combination)) for combination in expected
        )
        self.assertEqual(normalized_actual, normalized_expected)

    def test_candidates_with_duplicates(self) -> None:
        actual = self.solution.combinationSum2(
            [9, 2, 2, 4, 6, 1, 5], 8
        )
        self.assertCombinationsEqual(
            actual,
            [[1, 2, 5], [2, 2, 4], [2, 6]],
        )

    def test_distinct_candidates(self) -> None:
        actual = self.solution.combinationSum2([1, 2, 3, 4, 5], 7)
        self.assertCombinationsEqual(actual, [[1, 2, 4], [2, 5], [3, 4]])

    def test_duplicate_values_produce_unique_results(self) -> None:
        actual = self.solution.combinationSum2([1, 1, 1, 2], 3)
        self.assertCombinationsEqual(actual, [[1, 1, 1], [1, 2]])

    def test_candidate_cannot_be_reused(self) -> None:
        actual = self.solution.combinationSum2([2, 3], 4)
        self.assertEqual(actual, [])

    def test_no_combination(self) -> None:
        actual = self.solution.combinationSum2([4, 5], 3)
        self.assertEqual(actual, [])

    def test_input_is_not_modified(self) -> None:
        candidates = [3, 1, 2, 1]
        original = candidates.copy()

        self.solution.combinationSum2(candidates, 4)

        self.assertEqual(candidates, original)


if __name__ == "__main__":
    unittest.main()
