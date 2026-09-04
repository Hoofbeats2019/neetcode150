import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_single_zero(self) -> None:
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_two_values(self) -> None:
        self.assertEqual(self.solution.productExceptSelf([2, 3]), [3, 2])


if __name__ == "__main__":
    unittest.main()
