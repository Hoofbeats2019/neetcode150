"""Balanced Binary Tree.

Created: 9 August 2026
Created by: Yanlong Su

Given a binary tree, return True if it is height-balanced and False otherwise.

A height-balanced binary tree is a binary tree in which the left and right
subtrees of every node differ in height by no more than 1.

Example 1:
    Input: root = [1, 2, 3, null, null, 4]
    Output: True

Example 2:
    Input: root = [1, 2, 3, null, null, 4, null, 5]
    Output: False

Example 3:
    Input: root = []
    Output: True

Executable example:
    >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    >>> Solution().isBalanced(root)
    True

Constraints:
    0 <= The number of nodes in the tree <= 1000
    -1000 <= Node.val <= 1000

Time complexity: O(n)
Space complexity: O(h), where h is the height of the tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return True, 0

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            current_balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )
            current_height = 1 + max(left_height, right_height)

            return current_balanced, current_height

        balanced, _ = dfs(root)
        return balanced


def test_example_1() -> None:
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))

    assert Solution().isBalanced(root) is True


def test_example_2() -> None:
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3, TreeNode(4, TreeNode(5))),
    )

    assert Solution().isBalanced(root) is False


def test_example_3() -> None:
    assert Solution().isBalanced(None) is True


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
