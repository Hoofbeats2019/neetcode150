import unittest

from solutions.binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.search([-1, 0, 2, 4, 6, 8], 4), 3)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.search([-1, 0, 2, 4, 6, 8], 3), -1)

    def test_single_element_found(self) -> None:
        self.assertEqual(self.solution.search([5], 5), 0)

    def test_single_element_not_found(self) -> None:
        self.assertEqual(self.solution.search([5], 3), -1)

    def test_first_element(self) -> None:
        self.assertEqual(self.solution.search([1, 3, 5, 7, 9], 1), 0)

    def test_last_element(self) -> None:
        self.assertEqual(self.solution.search([1, 3, 5, 7, 9], 9), 4)

    def test_target_smaller_than_every_element(self) -> None:
        self.assertEqual(self.solution.search([1, 3, 5, 7, 9], -1), -1)

    def test_target_larger_than_every_element(self) -> None:
        self.assertEqual(self.solution.search([1, 3, 5, 7, 9], 11), -1)


if __name__ == "__main__":
    unittest.main()
