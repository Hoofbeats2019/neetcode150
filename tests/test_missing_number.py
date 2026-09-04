"""Unit tests for Missing Number."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.missing_number import Solution


class TestMissingNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(self.solution.missingNumber([1, 2, 3]), 0)

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.missingNumber([0, 2]), 1)

    def test_missing_largest_number(self) -> None:
        self.assertEqual(self.solution.missingNumber([0, 1, 2, 3]), 4)

    def test_single_element_array(self) -> None:
        self.assertEqual(self.solution.missingNumber([1]), 0)


if __name__ == "__main__":
    unittest.main()
