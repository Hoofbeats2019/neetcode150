"""Unit tests for Kth Largest Element in an Array.

Test pseudocode:
    for each worked example:
        request the kth largest element
        verify the expected value is returned

    for edge cases:
        verify a single element is returned
        verify duplicate values count as separate positions
        verify negative values are ordered correctly
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.kth_largest_element_in_an_array import Solution


class TestKthLargestElementInAnArray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        actual = self.solution.findKthLargest([2, 3, 1, 5, 4], 2)
        self.assertEqual(actual, 4)

    def test_second_example(self) -> None:
        actual = self.solution.findKthLargest([2, 3, 1, 1, 5, 5, 4], 3)
        self.assertEqual(actual, 4)

    def test_single_element(self) -> None:
        actual = self.solution.findKthLargest([7], 1)
        self.assertEqual(actual, 7)

    def test_duplicates_count_separately(self) -> None:
        actual = self.solution.findKthLargest([5, 5, 4], 2)
        self.assertEqual(actual, 5)

    def test_negative_values(self) -> None:
        actual = self.solution.findKthLargest([-3, -1, -2], 2)
        self.assertEqual(actual, -2)


if __name__ == "__main__":
    unittest.main()
