"""Unit tests for Implement Trie (Prefix Tree).

Test pseudocode:
    for the worked example:
        insert dog
        distinguish dog from its uninserted prefix do
        verify do is a prefix
        insert do and verify it becomes a complete word

    for shared paths:
        insert words with common prefixes and different branches
        verify every complete word and relevant prefix

    for edge cases:
        verify a missing path and an incomplete word
        verify duplicate insertion preserves the word
        verify a one-character word and prefix
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.implement_trie_prefix_tree import PrefixTree


class TestPrefixTree(unittest.TestCase):
    def test_example(self) -> None:
        prefix_tree = PrefixTree()
        prefix_tree.insert("dog")

        self.assertTrue(prefix_tree.search("dog"))
        self.assertFalse(prefix_tree.search("do"))
        self.assertTrue(prefix_tree.startsWith("do"))

        prefix_tree.insert("do")
        self.assertTrue(prefix_tree.search("do"))

    def test_words_share_paths_and_branch(self) -> None:
        prefix_tree = PrefixTree()
        prefix_tree.insert("dog")
        prefix_tree.insert("dot")
        prefix_tree.insert("cat")

        self.assertTrue(prefix_tree.search("dog"))
        self.assertTrue(prefix_tree.search("dot"))
        self.assertTrue(prefix_tree.search("cat"))
        self.assertTrue(prefix_tree.startsWith("do"))
        self.assertTrue(prefix_tree.startsWith("ca"))

    def test_missing_word_and_prefix(self) -> None:
        prefix_tree = PrefixTree()
        prefix_tree.insert("apple")

        self.assertFalse(prefix_tree.search("app"))
        self.assertFalse(prefix_tree.search("apply"))
        self.assertFalse(prefix_tree.startsWith("bat"))

    def test_duplicate_insertion(self) -> None:
        prefix_tree = PrefixTree()
        prefix_tree.insert("tree")
        prefix_tree.insert("tree")

        self.assertTrue(prefix_tree.search("tree"))
        self.assertTrue(prefix_tree.startsWith("tre"))

    def test_one_character_word(self) -> None:
        prefix_tree = PrefixTree()
        prefix_tree.insert("a")

        self.assertTrue(prefix_tree.search("a"))
        self.assertTrue(prefix_tree.startsWith("a"))
        self.assertFalse(prefix_tree.search("b"))


if __name__ == "__main__":
    unittest.main()
