"""Unit tests for Valid Anagram."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.valid_anagram import Solution


class TestValidAnagram(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_worked_examples(self) -> None:
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_repeated_characters_must_match(self) -> None:
        self.assertFalse(self.solution.isAnagram("aacc", "ccac"))

    def test_empty_strings_are_anagrams(self) -> None:
        self.assertTrue(self.solution.isAnagram("", ""))


if __name__ == "__main__":
    unittest.main()
