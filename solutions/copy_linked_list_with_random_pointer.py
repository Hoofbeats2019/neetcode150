"""Copy Linked List with Random Pointer.

Created: 8 August 2026
Created by: Yanlong Su

Create a deep copy of a linked list in which every node has both a next
pointer and a random pointer. A random pointer may refer to any node in the
list or to None. No pointer in the copied list may refer to an original node.

Examples:
    Input: head = [[3, None], [7, 3], [4, 0], [5, 1]]
    Output: [[3, None], [7, 3], [4, 0], [5, 1]]

    Input: head = [[1, None], [2, 2], [3, 2]]
    Output: [[1, None], [2, 2], [3, 2]]

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import Optional


class Node:
    def __init__(
        self,
        x: int,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None,
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        original_to_copy = {}
        dummy = Node(0)
        copy_tail = dummy
        current = head

        # First pass: create copied nodes and connect their next pointers.
        while current is not None:
            copied_node = Node(current.val)
            original_to_copy[current] = copied_node
            copy_tail.next = copied_node

            copy_tail = copied_node
            current = current.next

        current = head

        # Second pass: connect each copied node to the copied random target.
        while current is not None:
            copied_node = original_to_copy[current]

            if current.random is not None:
                copied_node.random = original_to_copy[current.random]

            current = current.next

        return dummy.next


def serialize_list(head: Optional[Node]) -> list[list[Optional[int]]]:
    nodes = []
    node_to_index = {}
    current = head

    while current is not None:
        node_to_index[current] = len(nodes)
        nodes.append(current)
        current = current.next

    return [
        [node.val, node_to_index.get(node.random)]
        for node in nodes
    ]


def test_examples() -> None:
    first_nodes = [Node(3), Node(7), Node(4), Node(5)]
    for current, following in zip(first_nodes, first_nodes[1:]):
        current.next = following
    first_nodes[1].random = first_nodes[3]
    first_nodes[2].random = first_nodes[0]
    first_nodes[3].random = first_nodes[1]

    first_copy = Solution().copyRandomList(first_nodes[0])
    assert serialize_list(first_copy) == [[3, None], [7, 3], [4, 0], [5, 1]]

    second_nodes = [Node(1), Node(2), Node(3)]
    for current, following in zip(second_nodes, second_nodes[1:]):
        current.next = following
    second_nodes[1].random = second_nodes[2]
    second_nodes[2].random = second_nodes[2]

    second_copy = Solution().copyRandomList(second_nodes[0])
    assert serialize_list(second_copy) == [[1, None], [2, 2], [3, 2]]


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
