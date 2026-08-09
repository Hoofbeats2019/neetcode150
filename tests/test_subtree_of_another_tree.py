import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.subtree_of_another_tree import Solution, TreeNode


class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_subtree_exists(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3),
        )
        sub_root = TreeNode(2, TreeNode(4), TreeNode(5))

        self.assertTrue(self.solution.isSubtree(root, sub_root))

    def test_matching_values_with_extra_descendant(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)),
            TreeNode(3),
        )
        sub_root = TreeNode(2, TreeNode(4), TreeNode(5))

        self.assertFalse(self.solution.isSubtree(root, sub_root))

    def test_entire_tree_is_a_subtree(self) -> None:
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        sub_root = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertTrue(self.solution.isSubtree(root, sub_root))

    def test_matching_value_at_a_later_node(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3)),
            TreeNode(2, TreeNode(4), TreeNode(5)),
        )
        sub_root = TreeNode(2, TreeNode(4), TreeNode(5))

        self.assertTrue(self.solution.isSubtree(root, sub_root))

    def test_same_values_with_different_structure(self) -> None:
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        sub_root = TreeNode(2, right=TreeNode(3))

        self.assertFalse(self.solution.isSubtree(root, sub_root))

    def test_subtree_value_is_absent(self) -> None:
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        sub_root = TreeNode(4)

        self.assertFalse(self.solution.isSubtree(root, sub_root))


if __name__ == "__main__":
    unittest.main()
