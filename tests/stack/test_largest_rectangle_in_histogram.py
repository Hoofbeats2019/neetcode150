import unittest

from solutions.stack.largest_rectangle_in_histogram import Solution


class TestLargestRectangleArea(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(
            self.solution.largestRectangleArea([7, 1, 7, 2, 2, 4]),
            8,
        )

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.largestRectangleArea([1, 3, 7]), 7)

    def test_single_zero_height_bar(self) -> None:
        self.assertEqual(self.solution.largestRectangleArea([0]), 0)

    def test_single_positive_height_bar(self) -> None:
        self.assertEqual(self.solution.largestRectangleArea([7]), 7)

    def test_equal_heights(self) -> None:
        self.assertEqual(self.solution.largestRectangleArea([2, 2, 2]), 6)

    def test_shorter_bar_between_equal_heights(self) -> None:
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 2]), 3)

    def test_increasing_heights(self) -> None:
        self.assertEqual(self.solution.largestRectangleArea([1, 2, 3, 4]), 6)

    def test_decreasing_heights(self) -> None:
        self.assertEqual(self.solution.largestRectangleArea([4, 3, 2, 1]), 6)


if __name__ == "__main__":
    unittest.main()
