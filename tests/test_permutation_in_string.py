import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.permutation_in_string import Solution
class TestPermutationInString(unittest.TestCase):
 def setUp(self): self.solution=Solution()
 def test_yes(self): self.assertTrue(self.solution.checkInclusion("ab","eidbaooo"))
 def test_no(self): self.assertFalse(self.solution.checkInclusion("ab","eidboaoo"))
 def test_short(self): self.assertFalse(self.solution.checkInclusion("abc","ab"))
