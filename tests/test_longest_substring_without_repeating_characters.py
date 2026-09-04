import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.longest_substring_without_repeating_characters import Solution


class TestLongestSubstring(unittest.TestCase):
    def setUp(self) -> None: self.solution = Solution()
    def test_example(self) -> None: self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
    def test_repeated(self) -> None: self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
    def test_empty(self) -> None: self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

if __name__ == "__main__": unittest.main()
