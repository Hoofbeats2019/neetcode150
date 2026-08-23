"""Unit tests for Word Ladder."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.word_ladder import Solution


class TestWordLadder(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_transformation_sequence_exists(self) -> None:
        word_list = ["bat", "bag", "sag", "dag", "dot"]
        self.assertEqual(
            self.solution.ladderLength("cat", "sag", word_list),
            4,
        )

    def test_end_word_is_not_in_word_list(self) -> None:
        word_list = ["bat", "bag", "sat", "dag", "dot"]
        self.assertEqual(
            self.solution.ladderLength("cat", "sag", word_list),
            0,
        )

    def test_end_word_is_one_transformation_away(self) -> None:
        self.assertEqual(
            self.solution.ladderLength("cat", "bat", ["bat"]),
            2,
        )

    def test_end_word_is_present_but_unreachable(self) -> None:
        word_list = ["dog", "dot", "sag"]
        self.assertEqual(
            self.solution.ladderLength("cat", "sag", word_list),
            0,
        )


if __name__ == "__main__":
    unittest.main()
