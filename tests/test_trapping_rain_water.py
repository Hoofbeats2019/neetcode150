import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.trapping_rain_water import Solution


class TestTrappingRainWater(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_basin(self) -> None:
        self.assertEqual(self.solution.trap([4, 2, 0, 3, 2, 5]), 9)

    def test_no_trapping(self) -> None:
        self.assertEqual(self.solution.trap([1, 2, 3]), 0)


if __name__ == "__main__":
    unittest.main()
