import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.minimum_window_substring import Solution
class TestMinimumWindow(unittest.TestCase):
 def setUp(self): self.solution=Solution()
 def test_example(self): self.assertEqual(self.solution.minWindow("ADOBECODEBANC","ABC"),"BANC")
 def test_none(self): self.assertEqual(self.solution.minWindow("a","aa"),"")
 def test_one(self): self.assertEqual(self.solution.minWindow("a","a"),"a")
