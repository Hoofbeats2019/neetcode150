import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.diameter_of_binary_tree import Solution, TreeNode


class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_with_right_subtree(self) -> None:
        root = TreeNode(
            1,
            right=TreeNode(
                2,
                TreeNode(3, TreeNode(5)),
                TreeNode(4),
            ),
        )

        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_example_with_two_children(self) -> None:
        root = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)

    def test_single_node(self) -> None:
        self.assertEqual(self.solution.diameterOfBinaryTree(TreeNode(1)), 0)

    def test_skewed_tree(self) -> None:
        root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))

        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)

    def test_diameter_does_not_pass_through_root(self) -> None:
        root = TreeNode(
            1,
            left=TreeNode(
                2,
                TreeNode(3, TreeNode(5)),
                TreeNode(4, right=TreeNode(6)),
            ),
        )

        self.assertEqual(self.solution.diameterOfBinaryTree(root), 4)


if __name__ == "__main__":
    unittest.main()
