import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.longest_repeating_character_replacement import Solution


class TestCharacterReplacement(unittest.TestCase):
    def setUp(self): self.solution = Solution()
    def test_example(self): self.assertEqual(self.solution.characterReplacement("ABAB", 2), 4)
    def test_shrink_window(self): self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)
    def test_empty(self): self.assertEqual(self.solution.characterReplacement("", 2), 0)
