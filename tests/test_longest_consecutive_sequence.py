import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.longest_consecutive_sequence import Solution


class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_duplicates_do_not_extend_sequence(self) -> None:
        self.assertEqual(self.solution.longestConsecutive([1, 2, 0, 1]), 3)

    def test_empty_list(self) -> None:
        self.assertEqual(self.solution.longestConsecutive([]), 0)


if __name__ == "__main__":
    unittest.main()
