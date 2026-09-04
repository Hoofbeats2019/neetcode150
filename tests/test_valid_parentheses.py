import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.valid_parentheses import Solution
class TestValidParentheses(unittest.TestCase):
 def setUp(self): self.solution=Solution()
 def test_valid(self): self.assertTrue(self.solution.isValid("()[]{}"))
 def test_wrong_order(self): self.assertFalse(self.solution.isValid("(]"))
 def test_unclosed(self): self.assertFalse(self.solution.isValid("(("))
