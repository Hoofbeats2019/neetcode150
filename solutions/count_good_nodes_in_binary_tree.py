"""Count Good Nodes in Binary Tree.

Created: 15 August 2026
Created by: Yanlong Su

Within a binary tree, a node is good if the path from the root to that node
contains no node with a value greater than the node's value.

Given the root of a binary tree, return the number of good nodes in the tree.

Example 1:
    Input: root = [2, 1, 1, 3, null, 1, 5]
    Output: 3

Example 2:
    Input: root = [1, 2, -1, 3, 4]
    Output: 4

Executable example:
    >>> root = TreeNode(2, TreeNode(1, TreeNode(3)), TreeNode(1))
    >>> Solution().goodNodes(root)
    2

Constraints:
    1 <= The number of nodes in the tree <= 100,000
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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        good_node_count = 0

        def dfs(node: Optional[TreeNode], path_maximum: float) -> None:
            nonlocal good_node_count

            if node is None:
                return

            if node.val >= path_maximum:
                good_node_count += 1

            new_maximum = max(path_maximum, node.val)
            dfs(node.left, new_maximum)
            dfs(node.right, new_maximum)

        dfs(root, float("-inf"))
        return good_node_count


def test_example_1() -> None:
    root = TreeNode(
        2,
        TreeNode(1, left=TreeNode(3)),
        TreeNode(1, TreeNode(1), TreeNode(5)),
    )

    assert Solution().goodNodes(root) == 3


def test_example_2() -> None:
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(-1),
    )

    assert Solution().goodNodes(root) == 4


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
