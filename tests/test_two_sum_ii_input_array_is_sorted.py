import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.two_sum_ii_input_array_is_sorted import Solution


class TestTwoSumII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_negative_values(self) -> None:
        self.assertEqual(self.solution.twoSum([-1, 0], -1), [1, 2])

    def test_middle_pair(self) -> None:
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5])


if __name__ == "__main__":
    unittest.main()
