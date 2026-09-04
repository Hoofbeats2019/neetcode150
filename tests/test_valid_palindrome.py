import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_not_a_palindrome(self) -> None:
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_only_symbols(self) -> None:
        self.assertTrue(self.solution.isPalindrome(".,"))


if __name__ == "__main__":
    unittest.main()
