import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.kth_smallest_integer_in_bst import Solution, TreeNode


class TestKthSmallestIntegerInBST(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_smallest_value(self) -> None:
        root = TreeNode(
            3,
            TreeNode(1, right=TreeNode(2)),
            TreeNode(4),
        )

        self.assertEqual(self.solution.kthSmallest(root, 1), 1)

    def test_third_smallest_value(self) -> None:
        root = TreeNode(
            5,
            TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
            TreeNode(6),
        )

        self.assertEqual(self.solution.kthSmallest(root, 3), 3)

    def test_single_node_tree(self) -> None:
        self.assertEqual(self.solution.kthSmallest(TreeNode(7), 1), 7)

    def test_largest_value(self) -> None:
        root = TreeNode(2, TreeNode(1), TreeNode(3))

        self.assertEqual(self.solution.kthSmallest(root, 3), 3)

    def test_middle_value_in_balanced_tree(self) -> None:
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)),
        )

        self.assertEqual(self.solution.kthSmallest(root, 4), 4)


if __name__ == "__main__":
    unittest.main()
