import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.maximum_depth_of_binary_tree import Solution, TreeNode


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_tree(self) -> None:
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))

        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_empty_tree(self) -> None:
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self) -> None:
        self.assertEqual(self.solution.maxDepth(TreeNode(7)), 1)

    def test_uses_longer_subtree(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4))),
            TreeNode(5),
        )

        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_right_skewed_tree(self) -> None:
        root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))

        self.assertEqual(self.solution.maxDepth(root), 3)


if __name__ == "__main__":
    unittest.main()
