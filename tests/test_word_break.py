"""Unit tests for Word Break."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.word_break import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(
            self.solution.wordBreak("neetcode", ["neet", "code"])
        )

    def test_second_worked_example(self) -> None:
        self.assertTrue(
            self.solution.wordBreak(
                "applepenapple",
                ["apple", "pen", "ape"],
            )
        )

    def test_third_worked_example(self) -> None:
        self.assertFalse(
            self.solution.wordBreak(
                "catsincars",
                ["cats", "cat", "sin", "in", "car"],
            )
        )

    def test_word_can_be_reused(self) -> None:
        self.assertTrue(self.solution.wordBreak("appleapple", ["apple"]))

    def test_short_string_can_use_multiple_short_words(self) -> None:
        self.assertTrue(self.solution.wordBreak("aa", ["a", "bbb"]))

    def test_later_prefix_can_succeed_after_dead_end(self) -> None:
        self.assertTrue(
            self.solution.wordBreak("cars", ["car", "ca", "rs"])
        )

    def test_unmatched_final_character_is_invalid(self) -> None:
        self.assertFalse(
            self.solution.wordBreak("aaaaab", ["a", "aa", "aaa"])
        )

    def test_maximum_string_length(self) -> None:
        word_dict = ["a" * length for length in range(1, 21)]
        self.assertFalse(
            self.solution.wordBreak("a" * 199 + "b", word_dict)
        )


if __name__ == "__main__":
    unittest.main()
