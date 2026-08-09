"""Same Binary Tree.

Created: 9 August 2026
Created by: Yanlong Su

Given the roots of two binary trees p and q, return True if the trees are
equivalent and False otherwise.

Two binary trees are equivalent when they have the exact same structure and
their corresponding nodes have the same values.

Example 1:
    Input: p = [1, 2, 3], q = [1, 2, 3]
    Output: True

Example 2:
    Input: p = [4, 7], q = [4, null, 7]
    Output: False

Example 3:
    Input: p = [1, 2, 3], q = [1, 3, 2]
    Output: False

Executable example:
    >>> p = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> q = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> Solution().isSameTree(p, q)
    True

Constraints:
    0 <= The number of nodes in both trees <= 100
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
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same


def test_example_1() -> None:
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    assert Solution().isSameTree(p, q) is True


def test_example_2() -> None:
    p = TreeNode(4, TreeNode(7))
    q = TreeNode(4, right=TreeNode(7))

    assert Solution().isSameTree(p, q) is False


def test_example_3() -> None:
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(3), TreeNode(2))

    assert Solution().isSameTree(p, q) is False


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
