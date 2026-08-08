import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.find_minimum_in_rotated_sorted_array import Solution


class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.findMin([3, 4, 5, 6, 1, 2]), 1)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.findMin([4, 5, 0, 1, 2, 3]), 0)

    def test_unrotated_array(self) -> None:
        self.assertEqual(self.solution.findMin([4, 5, 6, 7]), 4)

    def test_single_element(self) -> None:
        self.assertEqual(self.solution.findMin([7]), 7)

    def test_two_elements_rotated(self) -> None:
        self.assertEqual(self.solution.findMin([2, 1]), 1)

    def test_minimum_at_final_position(self) -> None:
        self.assertEqual(self.solution.findMin([2, 3, 4, 5, 1]), 1)

    def test_negative_minimum(self) -> None:
        self.assertEqual(self.solution.findMin([3, 5, -4, -2, 0]), -4)


if __name__ == "__main__":
    unittest.main()
