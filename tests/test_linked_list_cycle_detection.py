import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.linked_list_cycle_detection import ListNode, Solution


class TestLinkedListCycleDetection(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_cycle_connects_tail_to_second_node(self) -> None:
        first = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)
        fourth = ListNode(4)
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = second

        self.assertTrue(self.solution.hasCycle(first))

    def test_list_without_cycle(self) -> None:
        head = ListNode(1, ListNode(2))

        self.assertFalse(self.solution.hasCycle(head))

    def test_empty_list(self) -> None:
        self.assertFalse(self.solution.hasCycle(None))

    def test_single_node_without_cycle(self) -> None:
        head = ListNode(7)

        self.assertFalse(self.solution.hasCycle(head))

    def test_single_node_with_cycle(self) -> None:
        head = ListNode(7)
        head.next = head

        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_connects_tail_to_head(self) -> None:
        first = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)
        first.next = second
        second.next = third
        third.next = first

        self.assertTrue(self.solution.hasCycle(first))


if __name__ == "__main__":
    unittest.main()
