"""Remove Nth Node From End of List.

Created: 8 August 2026
Created by: Yanlong Su

Given the head of a singly linked list and an integer n, remove the nth node
from the end of the list and return its head.

Examples:
    Input: head = [1, 2, 3, 4], n = 2
    Output: [1, 2, 4]

    Input: head = [5], n = 1
    Output: []

    Input: head = [1, 2], n = 2
    Output: [2]

Time complexity: O(sz)
Space complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int,
    ) -> Optional[ListNode]:
        slow = head
        fast = head
        previous = None

        # Keep fast n - 1 nodes ahead of slow.
        for _ in range(n - 1):
            fast = fast.next

        # Move both pointers until fast reaches the final node.
        while fast.next is not None:
            fast = fast.next
            previous = slow
            slow = slow.next

        # If slow is the head, the list's second node becomes the new head.
        if previous is None:
            return head.next

        previous.next = slow.next
        return head


def linked_list_values(head: Optional[ListNode]) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


def test_examples() -> None:
    first_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    first_result = Solution().removeNthFromEnd(first_head, 2)
    assert linked_list_values(first_result) == [1, 2, 4]

    second_head = ListNode(5)
    second_result = Solution().removeNthFromEnd(second_head, 1)
    assert linked_list_values(second_result) == []

    third_head = ListNode(1, ListNode(2))
    third_result = Solution().removeNthFromEnd(third_head, 2)
    assert linked_list_values(third_result) == [2]


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
