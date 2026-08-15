"""Kth Smallest Integer in BST.

NeetCode 150 problem: 56
Created: 15 August 2026
Created by: Yanlong Su

Given the root of a binary search tree and an integer k, return the kth
smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:
    - The left subtree of every node contains only nodes with keys less than
      the node's key.
    - The right subtree of every node contains only nodes with keys greater
      than the node's key.
    - Both the left and right subtrees are also binary search trees.

Example 1:
    Input: root = [3, 1, 4, null, 2], k = 1
    Output: 1

Example 2:
    Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 3
    Output: 3

Time complexity: O(n)
Space complexity: O(n)
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """Return the kth smallest value using recursive in-order traversal."""
        values = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return values[k - 1]


def test_example_1() -> None:
    root = TreeNode(
        3,
        TreeNode(1, right=TreeNode(2)),
        TreeNode(4),
    )

    assert Solution().kthSmallest(root, 1) == 1


def test_example_2() -> None:
    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
        TreeNode(6),
    )

    assert Solution().kthSmallest(root, 3) == 3


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
