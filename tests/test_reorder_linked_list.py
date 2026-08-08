import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.reorder_linked_list import ListNode, Solution


def nodes_from(head: ListNode | None) -> list[ListNode]:
    nodes = []

    while head is not None:
        nodes.append(head)
        head = head.next

    return nodes


class TestReorderLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_even_length_example(self) -> None:
        nodes = [ListNode(value) for value in [2, 4, 6, 8]]
        for current, following in zip(nodes, nodes[1:]):
            current.next = following

        result = self.solution.reorderList(nodes[0])

        self.assertIsNone(result)
        self.assertEqual(nodes_from(nodes[0]), [nodes[0], nodes[3], nodes[1], nodes[2]])

    def test_odd_length_example(self) -> None:
        nodes = [ListNode(value) for value in [2, 4, 6, 8, 10]]
        for current, following in zip(nodes, nodes[1:]):
            current.next = following

        self.solution.reorderList(nodes[0])

        self.assertEqual(
            nodes_from(nodes[0]),
            [nodes[0], nodes[4], nodes[1], nodes[3], nodes[2]],
        )

    def test_single_node(self) -> None:
        head = ListNode(7)

        self.solution.reorderList(head)

        self.assertEqual(nodes_from(head), [head])
        self.assertIsNone(head.next)

    def test_two_nodes(self) -> None:
        second = ListNode(2)
        head = ListNode(1, second)

        self.solution.reorderList(head)

        self.assertEqual(nodes_from(head), [head, second])

    def test_empty_list(self) -> None:
        self.assertIsNone(self.solution.reorderList(None))


if __name__ == "__main__":
    unittest.main()
