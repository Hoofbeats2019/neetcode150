import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.lowest_common_ancestor_in_binary_search_tree import (
    Solution,
    TreeNode,
    build_example_tree,
)


class TestLowestCommonAncestorInBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_nodes_on_opposite_sides_of_root(self) -> None:
        root = build_example_tree()

        result = self.solution.lowestCommonAncestor(root, root.left, root.right)

        self.assertIs(result, root)

    def test_one_node_is_the_ancestor(self) -> None:
        root = build_example_tree()

        result = self.solution.lowestCommonAncestor(
            root,
            root.left,
            root.left.right,
        )

        self.assertIs(result, root.left)

    def test_common_ancestor_is_in_left_subtree(self) -> None:
        root = build_example_tree()
        p = root.left.right.left
        q = root.left.right.right

        result = self.solution.lowestCommonAncestor(root, p, q)

        self.assertIs(result, root.left.right)

    def test_common_ancestor_is_in_right_subtree(self) -> None:
        root = build_example_tree()
        p = root.right.left
        q = root.right.right

        result = self.solution.lowestCommonAncestor(root, p, q)

        self.assertIs(result, root.right)

    def test_skewed_tree(self) -> None:
        deepest = TreeNode(4)
        root = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=deepest)))

        result = self.solution.lowestCommonAncestor(root, root.right, deepest)

        self.assertIs(result, root.right)


if __name__ == "__main__":
    unittest.main()
