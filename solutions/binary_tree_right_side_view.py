"""Binary Tree Right Side View.

Created: 9 August 2026
Created by: Yanlong Su

Given the root of a binary tree, return the values of the nodes visible from
the right side, ordered from top to bottom.

Example 1:
    Input: root = [1, 2, 3, null, 4, null, 5]
    Output: [1, 3, 5]

Example 2:
    Input: root = [1, 2, 3, 4, null, null, null, 5]
    Output: [1, 3, 4, 5]

Example 3:
    Input: root = [1, null, 2]
    Output: [1, 2]

Example 4:
    Input: root = []
    Output: []

Executable example:
    >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> Solution().rightSideView(root)
    [1, 3]

Constraints:
    0 <= The number of nodes in the tree <= 100
    -100 <= Node.val <= 100

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
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        if root is None:
            return result

        queue = deque([root])

        while queue:
            level_size = len(queue)
            first_node = queue[0]
            result.append(first_node.val)

            for _ in range(level_size):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return result


def test_example_1() -> None:
    root = TreeNode(
        1,
        TreeNode(2, right=TreeNode(4)),
        TreeNode(3, right=TreeNode(5)),
    )

    assert Solution().rightSideView(root) == [1, 3, 5]


def test_example_2() -> None:
    root = TreeNode(
        1,
        TreeNode(2, left=TreeNode(4, left=TreeNode(5))),
        TreeNode(3),
    )

    assert Solution().rightSideView(root) == [1, 3, 4, 5]


def test_example_3() -> None:
    root = TreeNode(1, right=TreeNode(2))

    assert Solution().rightSideView(root) == [1, 2]


def test_example_4() -> None:
    assert Solution().rightSideView(None) == []


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_example_4()
    print("All example tests passed.")
