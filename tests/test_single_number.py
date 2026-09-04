"""Unit tests for Single Number."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.single_number import Solution


class TestSingleNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.singleNumber([3, 2, 3]), 2)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.singleNumber([7, 6, 6, 7, 8]), 8)

    def test_single_value(self) -> None:
        self.assertEqual(self.solution.singleNumber([42]), 42)

    def test_negative_unique_value(self) -> None:
        self.assertEqual(self.solution.singleNumber([-4, 1, 1, -4, -9]), -9)


if __name__ == "__main__":
    unittest.main()
