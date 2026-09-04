import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.container_with_most_water import Solution


class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_two_lines(self) -> None:
        self.assertEqual(self.solution.maxArea([1, 1]), 1)

    def test_increasing_heights(self) -> None:
        self.assertEqual(self.solution.maxArea([1, 2, 3, 4, 5]), 6)


if __name__ == "__main__":
    unittest.main()
