import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.three_sum import Solution


class TestThreeSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(self.solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_no_triplet(self) -> None:
        self.assertEqual(self.solution.threeSum([0, 1, 1]), [])

    def test_all_zeroes(self) -> None:
        self.assertEqual(self.solution.threeSum([0, 0, 0, 0]), [[0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
