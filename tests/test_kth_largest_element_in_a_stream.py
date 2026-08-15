"""Unit tests for Kth Largest Element in a Stream.

Test pseudocode:
    for the worked example:
        initialize the stream
        add each value in order
        verify the kth largest value after each addition

    for edge cases:
        verify k equals one
        verify duplicate and negative values count separately
        verify the initial stream does not need to be sorted
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.kth_largest_element_in_a_stream import KthLargest


class TestKthLargest(unittest.TestCase):
    def test_example(self) -> None:
        kth_largest = KthLargest(3, [1, 2, 3, 3])

        self.assertEqual(kth_largest.add(3), 3)
        self.assertEqual(kth_largest.add(5), 3)
        self.assertEqual(kth_largest.add(6), 3)
        self.assertEqual(kth_largest.add(7), 5)
        self.assertEqual(kth_largest.add(8), 6)

    def test_k_is_one(self) -> None:
        kth_largest = KthLargest(1, [])

        self.assertEqual(kth_largest.add(-2), -2)
        self.assertEqual(kth_largest.add(7), 7)

    def test_duplicates_and_negative_values(self) -> None:
        kth_largest = KthLargest(3, [-1, -1])

        self.assertEqual(kth_largest.add(-1), -1)
        self.assertEqual(kth_largest.add(-2), -1)

    def test_unsorted_initial_stream(self) -> None:
        kth_largest = KthLargest(2, [5, 1, 4, 2])

        self.assertEqual(kth_largest.add(3), 4)


if __name__ == "__main__":
    unittest.main()
