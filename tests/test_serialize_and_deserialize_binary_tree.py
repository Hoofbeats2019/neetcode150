import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.serialize_and_deserialize_binary_tree import Codec, TreeNode


class TestSerializeAndDeserializeBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.codec = Codec()

    def assert_round_trip(self, root: TreeNode | None) -> None:
        data = self.codec.serialize(root)
        rebuilt = self.codec.deserialize(data)

        self.assertEqual(self.codec.serialize(rebuilt), data)

    def test_balanced_tree(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2),
            TreeNode(3, TreeNode(4), TreeNode(5)),
        )

        self.assert_round_trip(root)

    def test_empty_tree(self) -> None:
        self.assertEqual(self.codec.serialize(None), "N")
        self.assertIsNone(self.codec.deserialize("N"))

    def test_single_node(self) -> None:
        self.assert_round_trip(TreeNode(7))

    def test_asymmetric_tree(self) -> None:
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))

        self.assert_round_trip(root)

    def test_negative_and_multi_digit_values(self) -> None:
        root = TreeNode(-10, TreeNode(25), TreeNode(-300))

        self.assert_round_trip(root)

    def test_deserialize_rebuilds_values_and_structure(self) -> None:
        root = self.codec.deserialize("1,N,2,3,N,N,N")

        self.assertIsNotNone(root)
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.right.val, 2)
        self.assertIsNotNone(root.right.left)
        self.assertEqual(root.right.left.val, 3)
        self.assertIsNone(root.right.right)


if __name__ == "__main__":
    unittest.main()
