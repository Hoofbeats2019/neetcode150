import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.median_of_two_sorted_arrays import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(
            self.solution.findMedianSortedArrays([1, 2], [3]), 2.0
        )

    def test_second_example(self) -> None:
        self.assertEqual(
            self.solution.findMedianSortedArrays([1, 3], [2, 4]), 2.5
        )

    def test_first_array_empty(self) -> None:
        self.assertEqual(self.solution.findMedianSortedArrays([], [1]), 1.0)

    def test_second_array_empty(self) -> None:
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2], []), 1.5)

    def test_duplicate_values(self) -> None:
        self.assertEqual(
            self.solution.findMedianSortedArrays([0, 0], [0, 0]), 0.0
        )

    def test_negative_values(self) -> None:
        self.assertEqual(
            self.solution.findMedianSortedArrays([-5, -3, -1], [-2]), -2.5
        )

    def test_shorter_array_is_second_argument(self) -> None:
        self.assertEqual(
            self.solution.findMedianSortedArrays([1, 2, 3, 4], [5]), 3.0
        )


if __name__ == "__main__":
    unittest.main()
