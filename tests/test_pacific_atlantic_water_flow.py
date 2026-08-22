"""Unit tests for Pacific Atlantic Water Flow.

Test pseudocode:
    for each worked example:
        compare the returned coordinate set with the expected cells

    for edge cases taken directly from the rules:
        verify a single cell touches both oceans
        verify every cell in a one-row island touches both oceans
        verify water can traverse cells of equal height
        verify the reversed search cannot move toward a lower cell
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.pacific_atlantic_water_flow import (
    Solution,
    example_heights_1,
    example_heights_2,
)


class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertCellsEqual(
        self,
        actual: list[list[int]],
        expected: set[tuple[int, int]],
    ) -> None:
        self.assertEqual({tuple(cell) for cell in actual}, expected)

    def test_first_worked_example(self) -> None:
        expected = {
            (0, 2),
            (0, 4),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 0),
        }
        self.assertCellsEqual(
            self.solution.pacificAtlantic(example_heights_1()),
            expected,
        )

    def test_single_column_worked_example(self) -> None:
        self.assertCellsEqual(
            self.solution.pacificAtlantic(example_heights_2()),
            {(0, 0), (1, 0)},
        )

    def test_single_cell_touches_both_oceans(self) -> None:
        self.assertCellsEqual(self.solution.pacificAtlantic([[7]]), {(0, 0)})

    def test_every_cell_in_one_row_touches_both_oceans(self) -> None:
        self.assertCellsEqual(
            self.solution.pacificAtlantic([[3, 1, 4]]),
            {(0, 0), (0, 1), (0, 2)},
        )

    def test_water_flows_across_equal_height_cells(self) -> None:
        self.assertCellsEqual(
            self.solution.pacificAtlantic([[5, 5], [5, 5]]),
            {(0, 0), (0, 1), (1, 0), (1, 1)},
        )

    def test_reversed_search_moves_only_to_equal_or_higher_cells(self) -> None:
        self.assertCellsEqual(
            self.solution.pacificAtlantic([[1, 2], [4, 3]]),
            {(0, 1), (1, 0), (1, 1)},
        )


if __name__ == "__main__":
    unittest.main()
