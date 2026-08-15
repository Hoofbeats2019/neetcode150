import sys
import unittest
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.construct_binary_tree_from_preorder_and_inorder_traversal import (
    Solution,
    TreeNode,
)


def serialize(root: Optional[TreeNode]) -> list[Optional[int]]:
    if root is None:
        return []

    result: list[Optional[int]] = []
    queue: list[Optional[TreeNode]] = [root]

    while queue:
        node = queue.pop(0)

        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


class TestConstructBinaryTreeFromPreorderAndInorderTraversal(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_asymmetric_tree(self) -> None:
        root = self.solution.buildTree(
            [1, 2, 3, 4],
            [2, 1, 3, 4],
        )

        self.assertEqual(serialize(root), [1, 2, 3, None, None, None, 4])

    def test_tree_with_two_non_leaf_children(self) -> None:
        root = self.solution.buildTree(
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
        )

        self.assertEqual(serialize(root), [3, 9, 20, None, None, 15, 7])

    def test_single_node(self) -> None:
        root = self.solution.buildTree([1], [1])

        self.assertEqual(serialize(root), [1])

    def test_empty_traversals(self) -> None:
        root = self.solution.buildTree([], [])

        self.assertIsNone(root)


if __name__ == "__main__":
    unittest.main()
