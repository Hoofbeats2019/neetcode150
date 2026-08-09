import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.balanced_binary_tree import Solution, TreeNode


class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_balanced_example(self) -> None:
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))

        self.assertTrue(self.solution.isBalanced(root))

    def test_unbalanced_example(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2),
            TreeNode(3, TreeNode(4, TreeNode(5))),
        )

        self.assertFalse(self.solution.isBalanced(root))

    def test_empty_tree(self) -> None:
        self.assertTrue(self.solution.isBalanced(None))

    def test_single_node(self) -> None:
        self.assertTrue(self.solution.isBalanced(TreeNode(1)))

    def test_height_difference_of_one(self) -> None:
        root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))

        self.assertTrue(self.solution.isBalanced(root))

    def test_unbalanced_descendant(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4))),
            TreeNode(5, right=TreeNode(6, right=TreeNode(7))),
        )

        self.assertFalse(self.solution.isBalanced(root))


if __name__ == "__main__":
    unittest.main()
