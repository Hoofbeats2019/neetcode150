"""Unit tests for Word Search.

Test pseudocode:
    for each worked example:
        search for the supplied word
        verify whether the word can be formed

    for edge cases taken directly from the rules:
        verify one cell can form a matching one-letter word
        verify a cell cannot be reused in the same word
        verify diagonal cells are not neighbors
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.word_search import Solution, example_board


class TestWordSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_word_is_present(self) -> None:
        self.assertTrue(self.solution.exist(example_board(), "CAT"))

    def test_word_is_not_present(self) -> None:
        self.assertFalse(self.solution.exist(example_board(), "BAT"))

    def test_single_cell_match(self) -> None:
        self.assertTrue(self.solution.exist([["A"]], "A"))

    def test_cell_cannot_be_reused(self) -> None:
        self.assertFalse(self.solution.exist([["A", "A"]], "AAA"))

    def test_diagonal_cells_are_not_neighbors(self) -> None:
        board = [["A", "X"], ["X", "B"]]
        self.assertFalse(self.solution.exist(board, "AB"))


if __name__ == "__main__":
    unittest.main()
