import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.merge_k_sorted_linked_lists import ListNode, Solution


def linked_list_from(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def values_from(head: ListNode | None) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


class TestMergeKSortedLinkedLists(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def merge(self, groups: list[list[int]]) -> list[int]:
        linked_lists = [linked_list_from(group) for group in groups]
        merged = self.solution.mergeKLists(linked_lists)
        return values_from(merged)

    def test_merges_multiple_sorted_lists(self) -> None:
        self.assertEqual(
            self.merge([[1, 2, 4], [1, 3, 5], [3, 6]]),
            [1, 1, 2, 3, 3, 4, 5, 6],
        )

    def test_empty_collection(self) -> None:
        self.assertEqual(self.merge([]), [])

    def test_collection_with_empty_list(self) -> None:
        self.assertEqual(self.merge([[]]), [])

    def test_handles_empty_lists_and_negative_values(self) -> None:
        self.assertEqual(
            self.merge([[], [-4, -1, 7], [], [-3, 2, 2]]),
            [-4, -3, -1, 2, 2, 7],
        )

    def test_handles_an_unpaired_list(self) -> None:
        self.assertEqual(
            self.merge([[1, 7], [2, 6], [3, 5], [4], [0, 8]]),
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
        )

    def test_reuses_existing_nodes(self) -> None:
        first = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)

        merged = self.solution.mergeKLists([second, first, third])

        self.assertIs(merged, first)
        self.assertIs(merged.next, second)
        self.assertIs(merged.next.next, third)


if __name__ == "__main__":
    unittest.main()
