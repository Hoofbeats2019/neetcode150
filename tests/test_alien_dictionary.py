"""Unit tests for Alien Dictionary."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.alien_dictionary import Solution


class TestAlienDictionary(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertValidOrder(self, words: list[str], order: str) -> None:
        expected_letters = {
            character for word in words for character in word
        }
        self.assertEqual(len(order), len(expected_letters))
        self.assertEqual(set(order), expected_letters)

        positions = {
            character: index for index, character in enumerate(order)
        }

        for first_word, second_word in zip(words, words[1:]):
            shared_length = min(len(first_word), len(second_word))

            if first_word[:shared_length] == second_word[:shared_length]:
                self.assertLessEqual(len(first_word), len(second_word))
                continue

            for index in range(shared_length):
                if first_word[index] != second_word[index]:
                    self.assertLess(
                        positions[first_word[index]],
                        positions[second_word[index]],
                    )
                    break

    def test_two_letters_have_one_order(self) -> None:
        self.assertEqual(
            self.solution.foreignDictionary(["z", "o"]),
            "zo",
        )

    def test_chain_of_letter_relationships(self) -> None:
        words = ["hrn", "hrf", "er", "enn", "rfnn"]
        self.assertEqual(
            self.solution.foreignDictionary(words),
            "hernf",
        )

    def test_longer_word_before_its_prefix_is_invalid(self) -> None:
        self.assertEqual(
            self.solution.foreignDictionary(["abc", "ab"]),
            "",
        )

    def test_cycle_is_invalid(self) -> None:
        self.assertEqual(
            self.solution.foreignDictionary(["z", "x", "z"]),
            "",
        )

    def test_single_word_includes_every_unique_letter(self) -> None:
        words = ["banana"]
        order = self.solution.foreignDictionary(words)
        self.assertValidOrder(words, order)

    def test_disconnected_letters_are_included(self) -> None:
        words = ["za", "zb", "ca", "cb"]
        order = self.solution.foreignDictionary(words)
        self.assertValidOrder(words, order)

    def test_duplicate_words_add_no_relationship(self) -> None:
        words = ["same", "same"]
        order = self.solution.foreignDictionary(words)
        self.assertValidOrder(words, order)


if __name__ == "__main__":
    unittest.main()
