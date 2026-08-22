"""Unit tests for Word Search II.

Test pseudocode:
    for each worked example:
        search the board for all supplied words
        compare the words found without depending on result order

    for edge cases taken directly from the rules:
        verify a one-cell board can match a one-letter word
        verify a cell cannot be reused in the same word
        verify shared word prefixes can produce multiple complete words
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.word_search_ii import Solution, example_board_1


class TestWordSearchII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_words_are_present(self) -> None:
        words = ["bat", "cat", "back", "backend", "stack"]
        actual = self.solution.findWords(example_board_1(), words)
        self.assertEqual(set(actual), {"cat", "back", "backend"})

    def test_word_is_not_present(self) -> None:
        board = [["x", "o"], ["x", "o"]]
        self.assertEqual(self.solution.findWords(board, ["xoxo"]), [])

    def test_single_cell_match(self) -> None:
        self.assertEqual(self.solution.findWords([["a"]], ["a"]), ["a"])

    def test_cell_cannot_be_reused(self) -> None:
        actual = self.solution.findWords([["a", "a"]], ["aa", "aaa"])
        self.assertEqual(actual, ["aa"])

    def test_words_with_shared_prefixes(self) -> None:
        board = [["a", "p", "p", "l", "e"]]
        actual = self.solution.findWords(board, ["app", "apple", "apply"])
        self.assertEqual(set(actual), {"app", "apple"})

    def test_word_is_returned_only_once(self) -> None:
        board = [["a", "a"], ["a", "a"]]
        self.assertEqual(self.solution.findWords(board, ["aa"]), ["aa"])


if __name__ == "__main__":
    unittest.main()
