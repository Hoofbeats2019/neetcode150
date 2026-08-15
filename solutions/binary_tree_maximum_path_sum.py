"""Binary Tree Maximum Path Sum.

Created: 15 August 2026
Created by: Yanlong Su
NeetCode 150 problem: 58

Given the root of a non-empty binary tree, return the maximum path sum of any
non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes has an edge connecting them. A node cannot appear in the sequence more
than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node values in the path.

Example 1:
    Input: root = [1, 2, 3]
    Output: 6

Example 2:
    Input: root = [-3]
    Output: -3

Executable example:
    >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> Solution().maxPathSum(root)
    6

Constraints:
    The tree contains at least one node.

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal global_max

            if node is None:
                return 0

            left_gain = dfs(node.left)
            right_gain = dfs(node.right)

            path_through_node = (
                node.val + max(left_gain, 0) + max(right_gain, 0)
            )
            global_max = max(global_max, path_through_node)

            upward_gain = node.val + max(left_gain, right_gain, 0)
            return upward_gain

        dfs(root)
        return int(global_max)


def test_example_1() -> None:
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    assert Solution().maxPathSum(root) == 6


def test_example_2() -> None:
    assert Solution().maxPathSum(TreeNode(-3)) == -3


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
