import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.search([3, 4, 5, 6, 1, 2], 1), 4)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.search([3, 5, 6, 0, 1, 2], 4), -1)

    def test_target_in_left_sorted_half(self) -> None:
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 5), 1)

    def test_target_in_right_sorted_half(self) -> None:
        self.assertEqual(self.solution.search([6, 7, 0, 1, 2, 4, 5], 4), 5)

    def test_unrotated_array(self) -> None:
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 4), 3)

    def test_single_element_found(self) -> None:
        self.assertEqual(self.solution.search([7], 7), 0)

    def test_single_element_not_found(self) -> None:
        self.assertEqual(self.solution.search([7], 3), -1)

    def test_target_at_rotation_point(self) -> None:
        self.assertEqual(self.solution.search([3, 4, 5, -2, -1, 0, 1], -2), 3)

    def test_target_at_first_position(self) -> None:
        self.assertEqual(self.solution.search([4, 5, 1, 2, 3], 4), 0)

    def test_target_at_last_position(self) -> None:
        self.assertEqual(self.solution.search([4, 5, 1, 2, 3], 3), 4)


if __name__ == "__main__":
    unittest.main()
