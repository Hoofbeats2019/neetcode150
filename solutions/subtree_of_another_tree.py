"""Subtree of Another Tree.

Return whether ``subRoot`` occurs in ``root`` with identical values and tree
structure.
"""

from typing import Optional

from solutions.same_binary_tree import TreeNode


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
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _same_tree(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        if first is None or second is None:
            return first is second
        return (
            first.val == second.val
            and self._same_tree(first.left, second.left)
            and self._same_tree(first.right, second.right)
        )
