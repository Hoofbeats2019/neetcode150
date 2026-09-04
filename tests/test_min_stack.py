import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.min_stack import MinStack
class TestMinStack(unittest.TestCase):
 def test_operations(self):
  stack=MinStack(); stack.push(-2); stack.push(0); stack.push(-3)
  self.assertEqual(stack.getMin(),-3); stack.pop(); self.assertEqual(stack.top(),0); self.assertEqual(stack.getMin(),-2)
