"""Subtree of Another Tree.

Created: 9 August 2026
Created by: Yanlong Su

Given the roots of two binary trees root and subRoot, return True if there is a
subtree of root with the same structure and node values as subRoot, and False
otherwise.

A subtree consists of a node and all of that node's descendants. A tree is also
considered a subtree of itself.

Example 1:
    Input: root = [1, 2, 3, 4, 5], subRoot = [2, 4, 5]
    Output: True

Example 2:
    Input: root = [1, 2, 3, 4, 5, null, null, 6],
           subRoot = [2, 4, 5]
    Output: False

Executable example:
    >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    >>> sub_root = TreeNode(2, TreeNode(4), TreeNode(5))
    >>> Solution().isSubtree(root, sub_root)
    True

Constraints:
    1 <= The number of nodes in both trees <= 100
    -100 <= Node.val <= 100

Time complexity: O(n * m) in the worst case
Space complexity: O(h + k), where h and k are the tree heights
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
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode],
    ) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        if self._same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(
            root.right,
            subRoot,
        )

    def _same_tree(
        self,
        first: Optional[TreeNode],
        second: Optional[TreeNode],
    ) -> bool:
        if first is None and second is None:
            return True

        if first is None or second is None:
            return False

        if first.val != second.val:
            return False

        return self._same_tree(first.left, second.left) and self._same_tree(
            first.right,
            second.right,
        )


def test_example_1() -> None:
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3),
    )
    sub_root = TreeNode(2, TreeNode(4), TreeNode(5))

    assert Solution().isSubtree(root, sub_root) is True


def test_example_2() -> None:
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)),
        TreeNode(3),
    )
    sub_root = TreeNode(2, TreeNode(4), TreeNode(5))

    assert Solution().isSubtree(root, sub_root) is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
