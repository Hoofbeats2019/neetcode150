"""Invert Binary Tree.

Created: 9 August 2026
Created by: Yanlong Su

You are given the root of a binary tree. Invert the binary tree and return its
root.

Example 1:
    Input: root = [1, 2, 3, 4, 5, 6, 7]
    Output: [1, 3, 2, 7, 6, 5, 4]

Example 2:
    Input: root = [3, 2, 1]
    Output: [3, 1, 2]

Example 3:
    Input: root = []
    Output: []

Executable example:
    >>> root = TreeNode(3, TreeNode(2), TreeNode(1))
    >>> inverted_root = Solution().invertTree(root)
    >>> inverted_root.val
    3
    >>> inverted_root.left.val
    1
    >>> inverted_root.right.val
    2

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


def test_example_1() -> None:
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )

    inverted_root = Solution().invertTree(root)

    assert inverted_root is root
    assert inverted_root.left is not None
    assert inverted_root.left.val == 3
    assert inverted_root.right is not None
    assert inverted_root.right.val == 2
    assert inverted_root.left.left is not None
    assert inverted_root.left.left.val == 7
    assert inverted_root.left.right is not None
    assert inverted_root.left.right.val == 6
    assert inverted_root.right.left is not None
    assert inverted_root.right.left.val == 5
    assert inverted_root.right.right is not None
    assert inverted_root.right.right.val == 4


def test_example_2() -> None:
    root = TreeNode(3, TreeNode(2), TreeNode(1))

    inverted_root = Solution().invertTree(root)

    assert inverted_root is root
    assert inverted_root.left is not None
    assert inverted_root.left.val == 1
    assert inverted_root.right is not None
    assert inverted_root.right.val == 2


def test_example_3() -> None:
    assert Solution().invertTree(None) is None


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
