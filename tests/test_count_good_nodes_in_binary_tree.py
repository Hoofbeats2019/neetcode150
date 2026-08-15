import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.count_good_nodes_in_binary_tree import Solution, TreeNode


class TestCountGoodNodesInBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self) -> None:
        root = TreeNode(
            2,
            TreeNode(1, left=TreeNode(3)),
            TreeNode(1, TreeNode(1), TreeNode(5)),
        )

        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_example_2(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(-1),
        )

        self.assertEqual(self.solution.goodNodes(root), 4)

    def test_single_node(self) -> None:
        self.assertEqual(self.solution.goodNodes(TreeNode(-100)), 1)

    def test_equal_to_path_maximum_is_good(self) -> None:
        root = TreeNode(2, TreeNode(2, TreeNode(2)))

        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_compares_with_all_ancestors(self) -> None:
        root = TreeNode(5, TreeNode(1, TreeNode(3)))

        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_good_descendant_of_bad_node(self) -> None:
        root = TreeNode(3, TreeNode(1, TreeNode(5)))

        self.assertEqual(self.solution.goodNodes(root), 2)

    def test_empty_tree(self) -> None:
        self.assertEqual(self.solution.goodNodes(None), 0)


if __name__ == "__main__":
    unittest.main()
