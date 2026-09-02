"""Unit tests for Valid Parenthesis String."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.valid_parenthesis_string import Solution


class TestValidParenthesisString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertTrue(self.solution.checkValidString("((**"))

    def test_second_worked_example(self) -> None:
        self.assertFalse(self.solution.checkValidString("(((*)"))

    def test_asterisk_can_be_an_opening_parenthesis(self) -> None:
        self.assertTrue(self.solution.checkValidString("*)"))

    def test_asterisk_can_be_empty(self) -> None:
        self.assertTrue(self.solution.checkValidString("*"))

    def test_closing_parenthesis_cannot_be_matched(self) -> None:
        self.assertFalse(self.solution.checkValidString(")*"))

    def test_asterisk_before_an_opening_parenthesis_cannot_close_it(self) -> None:
        self.assertFalse(self.solution.checkValidString("*("))


if __name__ == "__main__":
    unittest.main()
