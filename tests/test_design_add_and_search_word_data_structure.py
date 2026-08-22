"""Unit tests for Design Add and Search Word Data Structure."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.design_add_and_search_word_data_structure import WordDictionary


class TestWordDictionary(unittest.TestCase):
    def test_example(self) -> None:
        words = WordDictionary()
        words.addWord("day")
        words.addWord("bay")
        words.addWord("may")

        self.assertFalse(words.search("say"))
        self.assertTrue(words.search("day"))
        self.assertTrue(words.search(".ay"))
        self.assertTrue(words.search("b.."))

    def test_dot_matches_exactly_one_letter(self) -> None:
        words = WordDictionary()
        words.addWord("at")

        self.assertTrue(words.search(".t"))
        self.assertTrue(words.search("a."))
        self.assertFalse(words.search("."))
        self.assertFalse(words.search("..."))

    def test_dots_in_different_positions(self) -> None:
        words = WordDictionary()
        words.addWord("code")

        self.assertTrue(words.search(".ode"))
        self.assertTrue(words.search("c.de"))
        self.assertTrue(words.search("co.."))
        self.assertFalse(words.search("b.de"))

    def test_prefix_is_not_a_complete_word(self) -> None:
        words = WordDictionary()
        words.addWord("apple")

        self.assertFalse(words.search("app"))
        self.assertFalse(words.search("a.."))
        self.assertTrue(words.search("a...."))

    def test_one_character_word(self) -> None:
        words = WordDictionary()
        words.addWord("a")

        self.assertTrue(words.search("a"))
        self.assertTrue(words.search("."))
        self.assertFalse(words.search("b"))

    def test_shared_prefixes_and_duplicate_word(self) -> None:
        words = WordDictionary()
        words.addWord("car")
        words.addWord("cat")
        words.addWord("car")

        self.assertTrue(words.search("car"))
        self.assertTrue(words.search("cat"))
        self.assertTrue(words.search("ca."))
        self.assertFalse(words.search("can"))


if __name__ == "__main__":
    unittest.main()
