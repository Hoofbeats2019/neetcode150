"""Unit tests for Surrounded Regions.

Test pseudocode:
    for each worked example:
        capture every enclosed O region in place
        preserve every O region connected to an edge
        verify the method returns nothing

    for edge cases taken directly from the rules:
        preserve an O cell on the edge
        capture a single enclosed O cell
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.surrounded_regions import (
    Solution,
    example_board_1,
    example_board_2,
)


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_captures_only_surrounded_region(self) -> None:
        board = example_board_1()
        result = self.solution.solve(board)
        self.assertIsNone(result)
        self.assertEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        )

    def test_single_x_is_unchanged(self) -> None:
        board = example_board_2()
        self.solution.solve(board)
        self.assertEqual(board, [["X"]])

    def test_edge_connected_region_is_unchanged(self) -> None:
        board = [["O", "O"], ["X", "O"]]
        self.solution.solve(board)
        self.assertEqual(board, [["O", "O"], ["X", "O"]])

    def test_single_enclosed_o_is_captured(self) -> None:
        board = [
            ["X", "X", "X"],
            ["X", "O", "X"],
            ["X", "X", "X"],
        ]
        self.solution.solve(board)
        self.assertEqual(
            board,
            [
                ["X", "X", "X"],
                ["X", "X", "X"],
                ["X", "X", "X"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
