"""Valid Binary Search Tree.

Created: 15 August 2026
Created by: Yanlong Su

Given the root of a binary tree, return True if it is a valid binary search
tree, otherwise return False.

A valid binary search tree satisfies these constraints:
    - Every value in a node's left subtree is less than the node's value.
    - Every value in a node's right subtree is greater than the node's value.
    - Both subtrees are also valid binary search trees.

Example 1:
    Input: root = [2, 1, 3]
    Output: True

Example 2:
    Input: root = [1, 2, 3]
    Output: False

Executable example:
    >>> root = TreeNode(2, TreeNode(1), TreeNode(3))
    >>> Solution().isValidBST(root)
    True

Constraints:
    1 <= The number of nodes in the tree <= 10,000
    -1,000,000,000 <= Node.val <= 1,000,000,000

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Return whether root satisfies the binary-search-tree invariant."""
        def dfs(
            node: Optional[TreeNode],
            lower: float,
            upper: float,
        ) -> bool:
            if node is None:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(
                node.right,
                node.val,
                upper,
            )

        return dfs(root, float("-inf"), float("inf"))


def test_example_1() -> None:
    root = TreeNode(2, TreeNode(1), TreeNode(3))

    assert Solution().isValidBST(root) is True


def test_example_2() -> None:
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    assert Solution().isValidBST(root) is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
