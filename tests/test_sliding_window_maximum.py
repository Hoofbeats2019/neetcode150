import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.sliding_window_maximum import Solution
class TestSlidingWindowMaximum(unittest.TestCase):
 def setUp(self): self.solution=Solution()
 def test_example(self): self.assertEqual(self.solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3),[3,3,5,5,6,7])
 def test_single(self): self.assertEqual(self.solution.maxSlidingWindow([1],1),[1])
 def test_full(self): self.assertEqual(self.solution.maxSlidingWindow([9,11],2),[11])
