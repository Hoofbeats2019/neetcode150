"""Binary Tree Level Order Traversal.

Created: 9 August 2026
Created by: Yanlong Su

Given a binary tree root, return its level order traversal as a nested list,
where each sublist contains the values of nodes at a particular level in the
tree, from left to right.

Example 1:
    Input: root = [1, 2, 3, 4, 5, 6, 7]
    Output: [[1], [2, 3], [4, 5, 6, 7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Executable example:
    >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> Solution().levelOrder(root)
    [[1], [2, 3]]

Constraints:
    0 <= The number of nodes in the tree <= 2000
    -1000 <= Node.val <= 1000

Time complexity: O(n)
Space complexity: O(w), where w is the maximum width of the tree
"""

from collections import deque
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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result


def test_example_1() -> None:
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )

    assert Solution().levelOrder(root) == [[1], [2, 3], [4, 5, 6, 7]]


def test_example_2() -> None:
    assert Solution().levelOrder(TreeNode(1)) == [[1]]


def test_example_3() -> None:
    assert Solution().levelOrder(None) == []


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
