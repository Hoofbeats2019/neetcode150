import unittest

from solutions.koko_eating_bananas import Solution


class TestKokoEatingBananas(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.minEatingSpeed([1, 4, 3, 2], 9), 2)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.minEatingSpeed([25, 10, 23, 4], 4), 25)

    def test_single_pile(self) -> None:
        self.assertEqual(self.solution.minEatingSpeed([10], 4), 3)

    def test_one_hour_per_pile(self) -> None:
        self.assertEqual(self.solution.minEatingSpeed([3, 6, 7, 11], 4), 11)

    def test_slowest_rate_is_enough(self) -> None:
        self.assertEqual(self.solution.minEatingSpeed([1, 1, 1], 3), 1)

    def test_large_pile(self) -> None:
        self.assertEqual(
            self.solution.minEatingSpeed([1_000_000_000], 1),
            1_000_000_000,
        )


if __name__ == "__main__":
    unittest.main()
