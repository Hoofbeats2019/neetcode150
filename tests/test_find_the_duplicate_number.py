import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.find_the_duplicate_number import Solution


class TestFindTheDuplicateNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.findDuplicate([1, 2, 3, 2, 2]), 2)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.findDuplicate([1, 2, 3, 4, 4]), 4)

    def test_smallest_valid_input(self) -> None:
        self.assertEqual(self.solution.findDuplicate([1, 1]), 1)

    def test_duplicate_near_start(self) -> None:
        self.assertEqual(self.solution.findDuplicate([2, 1, 2, 3, 4]), 2)

    def test_input_is_not_modified(self) -> None:
        nums = [3, 1, 3, 4, 2]
        original = nums.copy()

        self.assertEqual(self.solution.findDuplicate(nums), 3)
        self.assertEqual(nums, original)


if __name__ == "__main__":
    unittest.main()
