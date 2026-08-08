"""Add Two Numbers.

Created: 8 August 2026
Created by: Yanlong Su

Add two non-negative integers represented by linked lists whose digits are
stored in reverse order. Return the sum in the same linked-list format.

Examples:
    Input: l1 = [1, 2, 3], l2 = [4, 5, 6]
    Output: [5, 7, 9]

    Input: l1 = [9], l2 = [9]
    Output: [8, 1]

Time complexity: O(max(n, m))
Space complexity: O(max(n, m)) for the returned linked list
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                total += l2.val
                l2 = l2.next

            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next

        return dummy.next


def linked_list_values(head: Optional[ListNode]) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


def test_examples() -> None:
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(4, ListNode(5, ListNode(6)))
    result = Solution().addTwoNumbers(l1, l2)
    assert linked_list_values(result) == [5, 7, 9]

    l1 = ListNode(9)
    l2 = ListNode(9)
    result = Solution().addTwoNumbers(l1, l2)
    assert linked_list_values(result) == [8, 1]


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
