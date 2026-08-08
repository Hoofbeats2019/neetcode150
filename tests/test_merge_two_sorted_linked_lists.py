import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.merge_two_sorted_linked_lists import ListNode, Solution


def values_from(head: ListNode | None) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


class TestMergeTwoSortedLinkedLists(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_merge_two_nonempty_lists(self) -> None:
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(5)))

        merged = self.solution.mergeTwoLists(list1, list2)

        self.assertEqual(values_from(merged), [1, 1, 2, 3, 4, 5])

    def test_first_list_is_empty(self) -> None:
        list2 = ListNode(1, ListNode(2))

        merged = self.solution.mergeTwoLists(None, list2)

        self.assertIs(merged, list2)
        self.assertEqual(values_from(merged), [1, 2])

    def test_second_list_is_empty(self) -> None:
        list1 = ListNode(1, ListNode(2))

        merged = self.solution.mergeTwoLists(list1, None)

        self.assertIs(merged, list1)
        self.assertEqual(values_from(merged), [1, 2])

    def test_both_lists_are_empty(self) -> None:
        self.assertIsNone(self.solution.mergeTwoLists(None, None))

    def test_reuses_existing_nodes(self) -> None:
        first = ListNode(1)
        second = ListNode(2)

        merged = self.solution.mergeTwoLists(first, second)

        self.assertIs(merged, first)
        self.assertIs(merged.next, second)


if __name__ == "__main__":
    unittest.main()
