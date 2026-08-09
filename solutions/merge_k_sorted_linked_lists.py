"""Merge K Sorted Linked Lists.

Created: 9 August 2026
Created by: Yanlong Su

Merge an array of sorted singly linked lists into one sorted linked list. The
result is built by relinking the existing nodes rather than copying them.

Examples:
    Input: lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
    Output: [1, 1, 2, 3, 3, 4, 5, 6]

    Input: lists = []
    Output: []

    Input: lists = [[]]
    Output: []

Time complexity: O(n log k), where n is the total number of nodes
Space complexity: O(1) auxiliary space
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def _merge_two_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 if list1 is not None else list2
        return dummy.next

    def mergeKLists(
        self,
        lists: List[Optional[ListNode]],
    ) -> Optional[ListNode]:
        if not lists:
            return None

        interval = 1

        while interval < len(lists):
            for index in range(0, len(lists) - interval, interval * 2):
                lists[index] = self._merge_two_lists(
                    lists[index],
                    lists[index + interval],
                )

            interval *= 2

        return lists[0]


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
    lists = [
        linked_list_from([1, 2, 4]),
        linked_list_from([1, 3, 5]),
        linked_list_from([3, 6]),
    ]
    merged = Solution().mergeKLists(lists)
    assert linked_list_values(merged) == [1, 1, 2, 3, 3, 4, 5, 6]

    merged = Solution().mergeKLists([])
    assert linked_list_values(merged) == []

    merged = Solution().mergeKLists([None])
    assert linked_list_values(merged) == []


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
