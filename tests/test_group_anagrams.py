"""Unit tests for Group Anagrams."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_worked_example(self) -> None:
        result = self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual({frozenset(group) for group in result}, {frozenset(["eat", "tea", "ate"]), frozenset(["tan", "nat"]), frozenset(["bat"])})

    def test_empty_input(self) -> None:
        self.assertEqual(self.solution.groupAnagrams([]), [])

    def test_empty_strings_share_a_group(self) -> None:
        self.assertEqual(self.solution.groupAnagrams(["", ""]), [["", ""]])


if __name__ == "__main__":
    unittest.main()
