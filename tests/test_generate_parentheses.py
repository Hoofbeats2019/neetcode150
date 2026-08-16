"""Unit tests for Generate Parentheses.

Test pseudocode:
    for each worked example:
        generate every well-formed parentheses string
        normalize the result ordering
        verify the expected strings are returned exactly once

    for an edge case:
        verify two pairs produce both well-formed strings
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertParenthesesEqual(
        self,
        actual: list[str],
        expected: list[str],
    ) -> None:
        self.assertEqual(sorted(actual), sorted(expected))

    def test_one_pair(self) -> None:
        actual = self.solution.generate_parenthesis(1)
        self.assertParenthesesEqual(actual, ["()"])

    def test_three_pairs(self) -> None:
        actual = self.solution.generate_parenthesis(3)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertParenthesesEqual(actual, expected)

    def test_two_pairs(self) -> None:
        actual = self.solution.generate_parenthesis(2)
        self.assertParenthesesEqual(actual, ["(())", "()()"])


if __name__ == "__main__":
    unittest.main()
