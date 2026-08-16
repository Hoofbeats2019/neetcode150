"""Unit tests for Find Median From Data Stream.

Test pseudocode:
    for the worked example:
        add each number to the stream
        verify the median after each requested lookup

    for edge cases:
        verify one number is its own median
        verify negative and positive numbers
        verify duplicate numbers
        verify numbers arriving in descending order
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.find_median_from_data_stream import MedianFinder


class TestMedianFinder(unittest.TestCase):
    def setUp(self) -> None:
        self.median_finder = MedianFinder()

    def test_example(self) -> None:
        self.median_finder.addNum(1)
        self.median_finder.addNum(2)
        self.assertEqual(self.median_finder.findMedian(), 1.5)

        self.median_finder.addNum(3)
        self.assertEqual(self.median_finder.findMedian(), 2.0)

    def test_single_number(self) -> None:
        self.median_finder.addNum(7)
        self.assertEqual(self.median_finder.findMedian(), 7.0)

    def test_negative_and_positive_numbers(self) -> None:
        for num in [-5, 10, -1, 4]:
            self.median_finder.addNum(num)

        self.assertEqual(self.median_finder.findMedian(), 1.5)

    def test_duplicate_numbers(self) -> None:
        for num in [2, 2, 2, 2]:
            self.median_finder.addNum(num)

        self.assertEqual(self.median_finder.findMedian(), 2.0)

    def test_descending_input(self) -> None:
        for num in [5, 4, 3, 2, 1]:
            self.median_finder.addNum(num)

        self.assertEqual(self.median_finder.findMedian(), 3.0)


if __name__ == "__main__":
    unittest.main()
