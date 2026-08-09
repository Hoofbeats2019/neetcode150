"""Lowest Common Ancestor in Binary Search Tree.

Created: 9 August 2026
Created by: Yanlong Su

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

The lowest common ancestor is the lowest node in the tree that has both p and q
as descendants. A node may be a descendant of itself.

Example 1:
    Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
    Output: 6

Example 2:
    Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
    Output: 2

Executable example:
    >>> root = TreeNode(6, TreeNode(2), TreeNode(8))
    >>> Solution().lowestCommonAncestor(root, root.left, root.right).val
    6

Constraints:
    2 <= The number of nodes in the tree <= 100,000
    -10^9 <= Node.val <= 10^9
    All Node.val values are unique.
    p and q are different nodes that exist in the BST.

Time complexity: O(h), where h is the tree height
Space complexity: O(1)
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current

        raise ValueError("p and q must exist in the binary search tree")


def build_example_tree() -> TreeNode:
    return TreeNode(
        6,
        TreeNode(
            2,
            TreeNode(0),
            TreeNode(4, TreeNode(3), TreeNode(5)),
        ),
        TreeNode(8, TreeNode(7), TreeNode(9)),
    )


def test_example_1() -> None:
    root = build_example_tree()

    assert Solution().lowestCommonAncestor(root, root.left, root.right) is root


def test_example_2() -> None:
    root = build_example_tree()

    assert (
        Solution().lowestCommonAncestor(root, root.left, root.left.right)
        is root.left
    )


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
