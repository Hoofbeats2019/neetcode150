import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.same_binary_tree import Solution, TreeNode


class TestSameBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_equivalent_trees(self) -> None:
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertTrue(self.solution.isSameTree(p, q))

    def test_different_structure(self) -> None:
        p = TreeNode(4, TreeNode(7))
        q = TreeNode(4, right=TreeNode(7))

        self.assertFalse(self.solution.isSameTree(p, q))

    def test_different_values(self) -> None:
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(3), TreeNode(2))

        self.assertFalse(self.solution.isSameTree(p, q))

    def test_both_trees_empty(self) -> None:
        self.assertTrue(self.solution.isSameTree(None, None))

    def test_only_one_tree_empty(self) -> None:
        self.assertFalse(self.solution.isSameTree(TreeNode(1), None))
        self.assertFalse(self.solution.isSameTree(None, TreeNode(1)))

    def test_equivalent_asymmetric_trees(self) -> None:
        p = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        q = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))

        self.assertTrue(self.solution.isSameTree(p, q))


if __name__ == "__main__":
    unittest.main()
