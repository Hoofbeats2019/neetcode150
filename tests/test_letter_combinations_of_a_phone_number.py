"""Unit tests for Letter Combinations of a Phone Number.

Test pseudocode:
    for each input string:
        request every possible keypad-letter combination
        normalize the result ordering
        verify the expected combinations are returned exactly once

    for direct edge cases:
        verify an empty input returns no combinations
        verify one digit returns each letter mapped to that digit
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfAPhoneNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertCombinationsEqual(
        self,
        actual: list[str],
        expected: list[str],
    ) -> None:
        self.assertEqual(sorted(actual), sorted(expected))

    def test_two_digits(self) -> None:
        actual = self.solution.letter_combinations("34")
        expected = [
            "dg",
            "dh",
            "di",
            "eg",
            "eh",
            "ei",
            "fg",
            "fh",
            "fi",
        ]
        self.assertCombinationsEqual(actual, expected)

    def test_empty_digits(self) -> None:
        self.assertEqual(self.solution.letter_combinations(""), [])

    def test_single_digit(self) -> None:
        actual = self.solution.letter_combinations("2")
        self.assertCombinationsEqual(actual, ["a", "b", "c"])

    def test_digits_with_four_letters(self) -> None:
        actual = self.solution.letter_combinations("79")
        expected = [
            first_letter + second_letter
            for first_letter in "pqrs"
            for second_letter in "wxyz"
        ]
        self.assertCombinationsEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
