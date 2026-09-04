import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.same_binary_tree import TreeNode
from solutions.subtree_of_another_tree import Solution


class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self): self.solution = Solution()
    def test_example(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        self.assertTrue(self.solution.isSubtree(root, TreeNode(4, TreeNode(1), TreeNode(2))))
    def test_different_structure(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
        self.assertFalse(self.solution.isSubtree(root, TreeNode(4, TreeNode(1), TreeNode(2))))
    def test_empty_subtree(self): self.assertTrue(self.solution.isSubtree(TreeNode(1), None))
