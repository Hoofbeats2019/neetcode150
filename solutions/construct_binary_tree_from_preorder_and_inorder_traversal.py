"""Construct Binary Tree from Preorder and Inorder Traversal.

Created: 15 August 2026
Created by: Yanlong Su

NeetCode 150 problem 57.

You are given two integer arrays, preorder and inorder. Preorder is the
preorder traversal of a binary tree, and inorder is the inorder traversal of
the same tree. Both arrays have the same size and contain unique values.
Rebuild the binary tree and return its root.

Example 1:
    Input: preorder = [1, 2, 3, 4], inorder = [2, 1, 3, 4]
    Output: [1, 2, 3, null, null, null, 4]

Example 2:
    Input: preorder = [3, 9, 20, 15, 7],
           inorder = [9, 3, 15, 20, 7]
    Output: [3, 9, 20, null, null, 15, 7]

Executable example:
    >>> root = Solution().buildTree([1, 2, 3, 4], [2, 1, 3, 4])
    >>> root.val
    1
    >>> root.left.val
    2
    >>> root.right.val
    3
    >>> root.right.right.val
    4

Constraints:
    preorder and inorder have the same length.
    Every value is unique within each traversal.
    Both arrays are valid traversals of the same binary tree.

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
    def buildTree(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        """Rebuild and return the binary tree described by both traversals."""
        inorder_index = {
            value: index for index, value in enumerate(inorder)
        }

        def build(
            pre_left: int,
            pre_right: int,
            in_left: int,
            in_right: int,
        ) -> Optional[TreeNode]:
            if pre_left >= pre_right:
                return None

            root_value = preorder[pre_left]
            root = TreeNode(root_value)

            root_inorder_index = inorder_index[root_value]
            left_size = root_inorder_index - in_left

            root.left = build(
                pre_left + 1,
                pre_left + 1 + left_size,
                in_left,
                root_inorder_index,
            )
            root.right = build(
                pre_left + 1 + left_size,
                pre_right,
                root_inorder_index + 1,
                in_right,
            )

            return root

        return build(0, len(preorder), 0, len(inorder))


def test_example_1() -> None:
    root = Solution().buildTree([1, 2, 3, 4], [2, 1, 3, 4])

    assert root is not None
    assert root.val == 1
    assert root.left is not None
    assert root.left.val == 2
    assert root.right is not None
    assert root.right.val == 3
    assert root.right.right is not None
    assert root.right.right.val == 4


def test_example_2() -> None:
    root = Solution().buildTree(
        [3, 9, 20, 15, 7],
        [9, 3, 15, 20, 7],
    )

    assert root is not None
    assert root.val == 3
    assert root.left is not None
    assert root.left.val == 9
    assert root.right is not None
    assert root.right.val == 20
    assert root.right.left is not None
    assert root.right.left.val == 15
    assert root.right.right is not None
    assert root.right.right.val == 7


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
