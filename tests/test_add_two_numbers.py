import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.add_two_numbers import ListNode, Solution


def linked_list_from(values: list[int]) -> ListNode:
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


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_add_same_length_lists(self) -> None:
        l1 = linked_list_from([1, 2, 3])
        l2 = linked_list_from([4, 5, 6])

        result = self.solution.addTwoNumbers(l1, l2)

        self.assertEqual(values_from(result), [5, 7, 9])

    def test_append_final_carry(self) -> None:
        l1 = linked_list_from([9])
        l2 = linked_list_from([9])

        result = self.solution.addTwoNumbers(l1, l2)

        self.assertEqual(values_from(result), [8, 1])

    def test_add_lists_with_different_lengths(self) -> None:
        l1 = linked_list_from([9, 9, 9])
        l2 = linked_list_from([1])

        result = self.solution.addTwoNumbers(l1, l2)

        self.assertEqual(values_from(result), [0, 0, 0, 1])

    def test_add_zero(self) -> None:
        l1 = linked_list_from([0])
        l2 = linked_list_from([0])

        result = self.solution.addTwoNumbers(l1, l2)

        self.assertEqual(values_from(result), [0])

    def test_carry_propagates_through_multiple_nodes(self) -> None:
        l1 = linked_list_from([5, 9, 9])
        l2 = linked_list_from([5])

        result = self.solution.addTwoNumbers(l1, l2)

        self.assertEqual(values_from(result), [0, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()
