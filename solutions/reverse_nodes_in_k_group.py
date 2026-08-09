"""Reverse Nodes in K-Group.

Created: 9 August 2026
Created by: Yanlong Su

Given the head of a singly linked list and a positive integer k, reverse the
nodes in consecutive groups of k. Leave a final group unchanged when it has
fewer than k nodes. Only the nodes' next pointers are modified.

Examples:
    Input: head = [1, 2, 3, 4, 5, 6], k = 3
    Output: [3, 2, 1, 6, 5, 4]

    Input: head = [1, 2, 3, 4, 5], k = 3
    Output: [3, 2, 1, 4, 5]

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            # Check that a complete group remains before changing any pointers.
            kth_node = group_previous

            for _ in range(k):
                kth_node = kth_node.next

                if kth_node is None:
                    return dummy.next

            next_group = kth_node.next
            previous = next_group
            current = group_previous.next

            # Reverse the current group by redirecting its next pointers.
            while current is not next_group:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            # Connect the previous group to this group and advance its boundary.
            old_group_head = group_previous.next
            group_previous.next = kth_node
            group_previous = old_group_head


def linked_list_from(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def linked_list_values(head: Optional[ListNode]) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


def test_examples() -> None:
    first_head = linked_list_from([1, 2, 3, 4, 5, 6])
    first_result = Solution().reverseKGroup(first_head, 3)
    assert linked_list_values(first_result) == [3, 2, 1, 6, 5, 4]

    second_head = linked_list_from([1, 2, 3, 4, 5])
    second_result = Solution().reverseKGroup(second_head, 3)
    assert linked_list_values(second_result) == [3, 2, 1, 4, 5]


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
