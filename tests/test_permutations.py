"""Unit tests for Permutations.

Test pseudocode:
    for each worked example:
        request every permutation
        normalize the result ordering
        verify the expected permutations are returned exactly once

    for edge cases:
        verify negative integers are handled
        verify the input list is not changed
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.permutations import Solution


class TestPermutations(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertPermutationsEqual(
        self,
        actual: list[list[int]],
        expected: list[list[int]],
    ) -> None:
        normalized_actual = sorted(tuple(permutation) for permutation in actual)
        normalized_expected = sorted(
            tuple(permutation) for permutation in expected
        )
        self.assertEqual(normalized_actual, normalized_expected)

    def test_three_integers(self) -> None:
        actual = self.solution.permute([1, 2, 3])
        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
        self.assertPermutationsEqual(actual, expected)

    def test_single_integer(self) -> None:
        self.assertEqual(self.solution.permute([7]), [[7]])

    def test_negative_and_positive_integers(self) -> None:
        actual = self.solution.permute([-1, 2])
        self.assertPermutationsEqual(actual, [[-1, 2], [2, -1]])

    def test_input_is_not_modified(self) -> None:
        nums = [3, 1, 2]
        original = nums.copy()

        self.solution.permute(nums)

        self.assertEqual(nums, original)


if __name__ == "__main__":
    unittest.main()
