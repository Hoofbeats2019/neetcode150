import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.invert_binary_tree import Solution, TreeNode


class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_complete_tree(self) -> None:
        four = TreeNode(4)
        five = TreeNode(5)
        six = TreeNode(6)
        seven = TreeNode(7)
        two = TreeNode(2, four, five)
        three = TreeNode(3, six, seven)
        root = TreeNode(1, two, three)

        inverted_root = self.solution.invertTree(root)

        self.assertIs(inverted_root, root)
        self.assertIs(root.left, three)
        self.assertIs(root.right, two)
        self.assertIs(three.left, seven)
        self.assertIs(three.right, six)
        self.assertIs(two.left, five)
        self.assertIs(two.right, four)

    def test_two_children(self) -> None:
        left = TreeNode(2)
        right = TreeNode(1)
        root = TreeNode(3, left, right)

        inverted_root = self.solution.invertTree(root)

        self.assertIs(inverted_root, root)
        self.assertIs(root.left, right)
        self.assertIs(root.right, left)

    def test_empty_tree(self) -> None:
        self.assertIsNone(self.solution.invertTree(None))

    def test_single_node(self) -> None:
        root = TreeNode(7)

        inverted_root = self.solution.invertTree(root)

        self.assertIs(inverted_root, root)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_node_with_only_left_child(self) -> None:
        child = TreeNode(2)
        root = TreeNode(1, left=child)

        inverted_root = self.solution.invertTree(root)

        self.assertIs(inverted_root, root)
        self.assertIsNone(root.left)
        self.assertIs(root.right, child)


if __name__ == "__main__":
    unittest.main()
