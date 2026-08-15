import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.valid_binary_search_tree import Solution, TreeNode


class TestValidBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_valid_three_node_tree(self) -> None:
        root = TreeNode(2, TreeNode(1), TreeNode(3))

        self.assertTrue(self.solution.isValidBST(root))

    def test_left_child_is_greater_than_parent(self) -> None:
        root = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertFalse(self.solution.isValidBST(root))

    def test_single_node_is_valid(self) -> None:
        self.assertTrue(self.solution.isValidBST(TreeNode(1)))

    def test_duplicate_value_is_invalid(self) -> None:
        root = TreeNode(2, TreeNode(2), TreeNode(3))

        self.assertFalse(self.solution.isValidBST(root))

    def test_descendant_must_respect_ancestor_ordering(self) -> None:
        root = TreeNode(
            10,
            TreeNode(5),
            TreeNode(15, TreeNode(6), TreeNode(20)),
        )

        self.assertFalse(self.solution.isValidBST(root))

    def test_left_descendant_must_respect_ancestor_ordering(self) -> None:
        root = TreeNode(
            10,
            TreeNode(5, TreeNode(2), TreeNode(12)),
            TreeNode(15),
        )

        self.assertFalse(self.solution.isValidBST(root))

    def test_valid_deeper_tree(self) -> None:
        root = TreeNode(
            10,
            TreeNode(5, TreeNode(2), TreeNode(7)),
            TreeNode(15, TreeNode(12), TreeNode(20)),
        )

        self.assertTrue(self.solution.isValidBST(root))


if __name__ == "__main__":
    unittest.main()
