import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.reverse_linked_list import ListNode, Solution


class TestReverseLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        first = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)
        fourth = ListNode(4)
        fifth = ListNode(5)
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth

        reversed_head = self.solution.reverseList(first)

        self.assertIs(reversed_head, fifth)
        self.assertIs(fifth.next, fourth)
        self.assertIs(fourth.next, third)
        self.assertIs(third.next, second)
        self.assertIs(second.next, first)
        self.assertIsNone(first.next)

    def test_empty_list(self) -> None:
        self.assertIsNone(self.solution.reverseList(None))

    def test_single_node(self) -> None:
        head = ListNode(7)

        reversed_head = self.solution.reverseList(head)

        self.assertIs(reversed_head, head)
        self.assertIsNone(reversed_head.next)

    def test_two_nodes(self) -> None:
        first = ListNode(1)
        second = ListNode(2)
        first.next = second

        reversed_head = self.solution.reverseList(first)

        self.assertIs(reversed_head, second)
        self.assertIs(second.next, first)
        self.assertIsNone(first.next)


if __name__ == "__main__":
    unittest.main()
