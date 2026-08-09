"""Diameter of Binary Tree.

Created: 9 August 2026
Created by: Yanlong Su

The diameter of a binary tree is the length of the longest path between any two
nodes in the tree. The path does not need to pass through the root. Path length
is measured by the number of edges between the nodes.

Given the root of a binary tree, return the diameter of the tree.

Example 1:
    Input: root = [1, null, 2, 3, 4, 5]
    Output: 3

Example 2:
    Input: root = [1, 2, 3]
    Output: 2

Executable example:
    >>> root = TreeNode(1, right=TreeNode(2, TreeNode(3), TreeNode(4)))
    >>> Solution().diameterOfBinaryTree(root)
    2

Constraints:
    1 <= The number of nodes in the tree <= 100
    -100 <= Node.val <= 100

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def calculate_depth(node: Optional[TreeNode]) -> int:
            nonlocal diameter

            if node is None:
                return -1

            left_depth = calculate_depth(node.left)
            right_depth = calculate_depth(node.right)

            current_diameter = left_depth + right_depth + 2
            diameter = max(diameter, current_diameter)

            return max(left_depth, right_depth) + 1

        calculate_depth(root)
        return diameter


def test_example_1() -> None:
    root = TreeNode(
        1,
        right=TreeNode(
            2,
            TreeNode(3, TreeNode(5)),
            TreeNode(4),
        ),
    )

    assert Solution().diameterOfBinaryTree(root) == 3


def test_example_2() -> None:
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    assert Solution().diameterOfBinaryTree(root) == 2


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
