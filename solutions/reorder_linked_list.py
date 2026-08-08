"""Reorder Linked List.

Created: 8 August 2026
Created by: Yanlong Su

Reorder a singly linked list in place by alternating nodes from its beginning
and end. Node values must not be changed.

Examples:
    Input: head = [2, 4, 6, 8]
    Output: [2, 8, 4, 6]

    Input: head = [2, 4, 6, 8, 10]
    Output: [2, 10, 4, 8, 6]

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # Split the list into two halves.
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        first_half = head
        second_half = slow.next
        slow.next = None

        # Reverse the second half.
        previous = None
        current = second_half

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        second_half = previous

        # Merge the two halves by alternating their nodes.
        while second_half is not None:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next


def linked_list_values(head: Optional[ListNode]) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


def test_examples() -> None:
    even_head = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
    Solution().reorderList(even_head)
    assert linked_list_values(even_head) == [2, 8, 4, 6]

    odd_head = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10)))))
    Solution().reorderList(odd_head)
    assert linked_list_values(odd_head) == [2, 10, 4, 8, 6]


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
