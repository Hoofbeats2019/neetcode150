"""Serialize and Deserialize Binary Tree.

Created: 15 August 2026
Created by: Yanlong Su

NeetCode 150 problem 59.

Implement an algorithm that converts a binary tree into a string and rebuilds
the original tree from that string. The serialized representation must retain
both the values and the structure of the tree.

Example 1:
    Input: root = [1, 2, 3, null, null, 4, 5]
    Output: [1, 2, 3, null, null, 4, 5]

Example 2:
    Input: root = []
    Output: []

Executable example:
    >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
    >>> codec = Codec()
    >>> data = codec.serialize(root)
    >>> data
    '1,2,N,N,3,N,N'
    >>> rebuilt = codec.deserialize(data)
    >>> rebuilt.val
    1

Constraints:
    The serialized string must contain enough information to reconstruct the
    original values and tree structure.
    The serialization format may be chosen freely.

Time complexity: O(n) for both serialize and deserialize
Space complexity: O(n) for both serialize and deserialize
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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Return a preorder representation containing null markers."""
        values: list[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                values.append("N")
                return

            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Rebuild a tree from its preorder representation."""
        values = data.split(",")
        index = 0

        def dfs() -> Optional[TreeNode]:
            nonlocal index

            value = values[index]
            index += 1

            if value == "N":
                return None

            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


def test_example_1() -> None:
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3, TreeNode(4), TreeNode(5)),
    )
    codec = Codec()

    data = codec.serialize(root)
    rebuilt = codec.deserialize(data)

    assert data == "1,2,N,N,3,4,N,N,5,N,N"
    assert codec.serialize(rebuilt) == data


def test_example_2() -> None:
    codec = Codec()

    data = codec.serialize(None)
    rebuilt = codec.deserialize(data)

    assert data == "N"
    assert rebuilt is None


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
