import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from solutions.daily_temperatures import Solution
class TestDailyTemperatures(unittest.TestCase):
 def test_example(self): self.assertEqual(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]),[1,1,4,2,1,1,0,0])
 def test_descending(self): self.assertEqual(Solution().dailyTemperatures([30,20,10]),[0,0,0])
