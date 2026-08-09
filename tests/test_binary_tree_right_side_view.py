import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.binary_tree_right_side_view import Solution, TreeNode


class TestBinaryTreeRightSideView(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_rightmost_nodes_on_both_subtrees(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, right=TreeNode(4)),
            TreeNode(3, right=TreeNode(5)),
        )

        self.assertEqual(self.solution.rightSideView(root), [1, 3, 5])

    def test_view_falls_back_to_left_subtree(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, left=TreeNode(4, left=TreeNode(5))),
            TreeNode(3),
        )

        self.assertEqual(self.solution.rightSideView(root), [1, 3, 4, 5])

    def test_right_skewed_tree(self) -> None:
        root = TreeNode(1, right=TreeNode(2))

        self.assertEqual(self.solution.rightSideView(root), [1, 2])

    def test_empty_tree(self) -> None:
        self.assertEqual(self.solution.rightSideView(None), [])

    def test_left_skewed_tree(self) -> None:
        root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

        self.assertEqual(self.solution.rightSideView(root), [1, 2, 3])

    def test_deeper_left_node_is_visible_when_right_subtree_ends(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, right=TreeNode(4, right=TreeNode(6))),
            TreeNode(3, left=TreeNode(5)),
        )

        self.assertEqual(self.solution.rightSideView(root), [1, 3, 5, 6])


if __name__ == "__main__":
    unittest.main()
