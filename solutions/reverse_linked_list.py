"""Reverse Linked List.

Created: 8 August 2026
Created by: Yanlong Su

Reverse a singly linked list and return its new head.

Example:
    Input: 1 -> 2 -> 3 -> None
    Output: 3 -> 2 -> 1 -> None

Executable example:
    >>> head = ListNode(1, ListNode(2, ListNode(3)))
    >>> reversed_head = Solution().reverseList(head)
    >>> reversed_head.val
    3
    >>> reversed_head.next.val
    2
    >>> reversed_head.next.next.val
    1
    >>> reversed_head.next.next.next is None
    True

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        return previous


def test_example() -> None:
    head = ListNode(1, ListNode(2, ListNode(3)))
    reversed_head = Solution().reverseList(head)

    assert reversed_head is not None
    assert reversed_head.val == 3
    assert reversed_head.next is not None
    assert reversed_head.next.val == 2
    assert reversed_head.next.next is not None
    assert reversed_head.next.next.val == 1
    assert reversed_head.next.next.next is None


if __name__ == "__main__":
    test_example()
    print("Example test passed.")
