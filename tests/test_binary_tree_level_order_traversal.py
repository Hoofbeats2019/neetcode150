import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.binary_tree_level_order_traversal import Solution, TreeNode


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_complete_tree(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )

        self.assertEqual(
            self.solution.levelOrder(root),
            [[1], [2, 3], [4, 5, 6, 7]],
        )

    def test_single_node(self) -> None:
        self.assertEqual(self.solution.levelOrder(TreeNode(1)), [[1]])

    def test_empty_tree(self) -> None:
        self.assertEqual(self.solution.levelOrder(None), [])

    def test_sparse_tree_preserves_left_to_right_order(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, right=TreeNode(4)),
            TreeNode(3, left=TreeNode(5)),
        )

        self.assertEqual(self.solution.levelOrder(root), [[1], [2, 3], [4, 5]])

    def test_duplicate_and_negative_values(self) -> None:
        root = TreeNode(-1, TreeNode(-1), TreeNode(0))

        self.assertEqual(self.solution.levelOrder(root), [[-1], [-1, 0]])


if __name__ == "__main__":
    unittest.main()
