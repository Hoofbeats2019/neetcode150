import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.reverse_nodes_in_k_group import ListNode, Solution


def linked_list_from(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def linked_list_values(head: ListNode | None) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


class TestReverseNodesInKGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_reverses_every_complete_group(self) -> None:
        head = linked_list_from([1, 2, 3, 4, 5, 6])

        result = self.solution.reverseKGroup(head, 3)

        self.assertEqual(linked_list_values(result), [3, 2, 1, 6, 5, 4])

    def test_leaves_incomplete_final_group_unchanged(self) -> None:
        head = linked_list_from([1, 2, 3, 4, 5])

        result = self.solution.reverseKGroup(head, 3)

        self.assertEqual(linked_list_values(result), [3, 2, 1, 4, 5])

    def test_k_equal_to_one_keeps_original_order(self) -> None:
        head = linked_list_from([1, 2, 3])

        result = self.solution.reverseKGroup(head, 1)

        self.assertIs(result, head)
        self.assertEqual(linked_list_values(result), [1, 2, 3])

    def test_reverses_entire_list_when_k_equals_length(self) -> None:
        head = linked_list_from([1, 2, 3, 4])

        result = self.solution.reverseKGroup(head, 4)

        self.assertEqual(linked_list_values(result), [4, 3, 2, 1])

    def test_relinks_existing_nodes_without_changing_values(self) -> None:
        first = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)
        fourth = ListNode(4)
        first.next = second
        second.next = third
        third.next = fourth

        result = self.solution.reverseKGroup(first, 3)

        self.assertIs(result, third)
        self.assertIs(third.next, second)
        self.assertIs(second.next, first)
        self.assertIs(first.next, fourth)
        self.assertEqual([first.val, second.val, third.val, fourth.val], [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
