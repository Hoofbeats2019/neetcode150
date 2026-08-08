import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.copy_linked_list_with_random_pointer import (
    Node,
    Solution,
    serialize_list,
)


def build_list(values: list[int], random_indices: list[int | None]) -> Node | None:
    if not values:
        return None

    nodes = [Node(value) for value in values]

    for current, following in zip(nodes, nodes[1:]):
        current.next = following

    for node, random_index in zip(nodes, random_indices):
        if random_index is not None:
            node.random = nodes[random_index]

    return nodes[0]


def list_nodes(head: Node | None) -> list[Node]:
    nodes = []

    while head is not None:
        nodes.append(head)
        head = head.next

    return nodes


class TestCopyLinkedListWithRandomPointer(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assert_deep_copy(self, original: Node, copied: Node) -> None:
        original_nodes = list_nodes(original)
        copied_nodes = list_nodes(copied)

        self.assertEqual(len(copied_nodes), len(original_nodes))
        self.assertTrue(set(original_nodes).isdisjoint(copied_nodes))

        for copied_node in copied_nodes:
            self.assertNotIn(copied_node.next, original_nodes)
            self.assertNotIn(copied_node.random, original_nodes)

    def test_first_example(self) -> None:
        head = build_list([3, 7, 4, 5], [None, 3, 0, 1])

        copied = self.solution.copyRandomList(head)

        self.assertEqual(
            serialize_list(copied),
            [[3, None], [7, 3], [4, 0], [5, 1]],
        )
        self.assert_deep_copy(head, copied)

    def test_second_example(self) -> None:
        head = build_list([1, 2, 3], [None, 2, 2])

        copied = self.solution.copyRandomList(head)

        self.assertEqual(serialize_list(copied), [[1, None], [2, 2], [3, 2]])
        self.assert_deep_copy(head, copied)

    def test_empty_list(self) -> None:
        self.assertIsNone(self.solution.copyRandomList(None))

    def test_duplicate_values_and_self_references(self) -> None:
        head = build_list([4, 4], [0, 1])

        copied = self.solution.copyRandomList(head)

        self.assertEqual(serialize_list(copied), [[4, 0], [4, 1]])
        self.assert_deep_copy(head, copied)


if __name__ == "__main__":
    unittest.main()
