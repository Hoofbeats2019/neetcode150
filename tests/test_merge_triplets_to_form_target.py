"""Unit tests for Merge Triplets to Form Target."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.merge_triplets_to_form_target import Solution


class TestMergeTripletsToFormTarget(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(
            self.solution.mergeTriplets([[1, 2, 3], [7, 1, 1]], [7, 2, 3])
        )

    def test_second_worked_example(self) -> None:
        self.assertFalse(
            self.solution.mergeTriplets(
                [[2, 5, 6], [1, 4, 4], [5, 7, 5]], [5, 4, 6]
            )
        )

    def test_one_triplet_already_matches_target(self) -> None:
        self.assertTrue(self.solution.mergeTriplets([[5, 4, 6]], [5, 4, 6]))

    def test_requires_three_safe_triplets(self) -> None:
        self.assertTrue(
            self.solution.mergeTriplets([[5, 1, 1], [1, 4, 1], [1, 1, 6]], [5, 4, 6])
        )

    def test_triplet_exceeding_one_coordinate_is_unsafe(self) -> None:
        self.assertFalse(
            self.solution.mergeTriplets([[5, 4, 7], [1, 1, 6]], [5, 4, 6])
        )


if __name__ == "__main__":
    unittest.main()
