"""Merge Two Sorted Linked Lists.

Created: 8 August 2026
Created by: Yanlong Su

Merge two sorted singly linked lists into one sorted linked list. The merged
list is made from the existing nodes in the two input lists.

Examples:
    Input: list1 = [1, 2, 4], list2 = [1, 3, 5]
    Output: [1, 1, 2, 3, 4, 5]

    Input: list1 = [], list2 = [1, 2]
    Output: [1, 2]

    Input: list1 = [], list2 = []
    Output: []

Time complexity: O(n + m)
Space complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_head = None
        result_tail = None

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                selected_node = list1
                list1 = list1.next
            else:
                selected_node = list2
                list2 = list2.next

            if result_head is None:
                result_head = selected_node
                result_tail = selected_node
            else:
                result_tail.next = selected_node
                result_tail = selected_node

        remaining_nodes = list1 if list1 is not None else list2

        if result_head is None:
            result_head = remaining_nodes
        else:
            result_tail.next = remaining_nodes

        return result_head


def linked_list_values(head: Optional[ListNode]) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


def test_examples() -> None:
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(5)))
    merged = Solution().mergeTwoLists(list1, list2)
    assert linked_list_values(merged) == [1, 1, 2, 3, 4, 5]

    list2 = ListNode(1, ListNode(2))
    merged = Solution().mergeTwoLists(None, list2)
    assert linked_list_values(merged) == [1, 2]

    merged = Solution().mergeTwoLists(None, None)
    assert linked_list_values(merged) == []


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
