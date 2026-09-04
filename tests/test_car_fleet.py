import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from solutions.car_fleet import Solution
class TestCarFleet(unittest.TestCase):
 def test_example(self): self.assertEqual(Solution().carFleet(12,[10,8,0,5,3],[2,4,1,1,3]),3)
 def test_one(self): self.assertEqual(Solution().carFleet(10,[3],[3]),1)
