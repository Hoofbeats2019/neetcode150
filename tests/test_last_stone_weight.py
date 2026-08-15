"""Unit tests for Last Stone Weight.

Test pseudocode:
    for each worked example:
        run the stone-smashing simulation
        verify the final remaining weight

    for edge cases:
        verify one stone remains unchanged
        verify two equal stones leave no stone
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.last_stone_weight import Solution


class TestLastStoneWeight(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.lastStoneWeight([2, 3, 6, 2, 4]), 1)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.lastStoneWeight([1, 2]), 1)

    def test_single_stone(self) -> None:
        self.assertEqual(self.solution.lastStoneWeight([7]), 7)

    def test_two_equal_stones(self) -> None:
        self.assertEqual(self.solution.lastStoneWeight([5, 5]), 0)


if __name__ == "__main__":
    unittest.main()
