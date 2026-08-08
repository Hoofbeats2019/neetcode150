"""Linked List Cycle Detection.

Created: 8 August 2026
Created by: Yanlong Su

Given the head of a singly linked list, return True if the list contains a
cycle. Otherwise, return False.

A cycle exists when following a node's next pointer eventually visits a node
that has already been visited. The cycle index used to construct an input is
not provided to the solution.

Examples:
    Input: head = [1, 2, 3, 4], index = 1
    Output: True

    Input: head = [1, 2], index = -1
    Output: False

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False


def test_examples() -> None:
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    assert Solution().hasCycle(first) is True

    first = ListNode(1, ListNode(2))

    assert Solution().hasCycle(first) is False


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
