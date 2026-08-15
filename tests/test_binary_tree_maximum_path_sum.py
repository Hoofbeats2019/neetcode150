import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.binary_tree_maximum_path_sum import Solution, TreeNode


class TestBinaryTreeMaximumPathSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_path_through_root(self) -> None:
        root = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertEqual(self.solution.maxPathSum(root), 6)

    def test_single_negative_node(self) -> None:
        self.assertEqual(self.solution.maxPathSum(TreeNode(-3)), -3)

    def test_best_path_does_not_include_root(self) -> None:
        root = TreeNode(
            -10,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7)),
        )

        self.assertEqual(self.solution.maxPathSum(root), 42)

    def test_all_negative_values(self) -> None:
        root = TreeNode(-8, TreeNode(-4), TreeNode(-6))

        self.assertEqual(self.solution.maxPathSum(root), -4)


if __name__ == "__main__":
    unittest.main()
