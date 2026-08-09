"""Maximum Depth of Binary Tree.

Created: 9 August 2026
Created by: Yanlong Su

Given the root of a binary tree, return its depth. The depth is the number of
nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [1, 2, 3, null, null, 4]
    Output: 3

Example 2:
    Input: root = []
    Output: 0

Executable example:
    >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    >>> Solution().maxDepth(root)
    3

Constraints:
    0 <= The number of nodes in the tree <= 100
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


def test_example_1() -> None:
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))

    assert Solution().maxDepth(root) == 3


def test_example_2() -> None:
    assert Solution().maxDepth(None) == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
