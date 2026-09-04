import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.evaluate_reverse_polish_notation import Solution
class TestEvaluateRPN(unittest.TestCase):
 def setUp(self): self.solution=Solution()
 def test_example(self): self.assertEqual(self.solution.evalRPN(["2","1","+","3","*"]),9)
 def test_division(self): self.assertEqual(self.solution.evalRPN(["4","13","5","/","+"]),6)
