import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.remove_nth_node_from_end_of_list import ListNode, Solution


def linked_list_values(head: ListNode | None) -> list[int]:
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_remove_middle_node(self) -> None:
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

        result = self.solution.removeNthFromEnd(head, 2)

        self.assertEqual(linked_list_values(result), [1, 2, 4])

    def test_remove_only_node(self) -> None:
        head = ListNode(5)

        result = self.solution.removeNthFromEnd(head, 1)

        self.assertIsNone(result)

    def test_remove_head(self) -> None:
        second = ListNode(2)
        head = ListNode(1, second)

        result = self.solution.removeNthFromEnd(head, 2)

        self.assertIs(result, second)
        self.assertEqual(linked_list_values(result), [2])

    def test_remove_tail(self) -> None:
        head = ListNode(1, ListNode(2, ListNode(3)))

        result = self.solution.removeNthFromEnd(head, 1)

        self.assertIs(result, head)
        self.assertEqual(linked_list_values(result), [1, 2])


if __name__ == "__main__":
    unittest.main()
