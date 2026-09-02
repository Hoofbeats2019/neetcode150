"""Unit tests for Gas Station."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.gas_station import Solution


class TestGasStation(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_worked_example(self) -> None:
        self.assertEqual(
            self.solution.canCompleteCircuit([1, 2, 3, 4], [2, 2, 4, 1]),
            3,
        )

    def test_second_worked_example(self) -> None:
        self.assertEqual(self.solution.canCompleteCircuit([1, 2, 3], [2, 3, 2]), -1)

    def test_single_station_with_enough_gas(self) -> None:
        self.assertEqual(self.solution.canCompleteCircuit([5], [5]), 0)

    def test_single_station_without_enough_gas(self) -> None:
        self.assertEqual(self.solution.canCompleteCircuit([2], [3]), -1)

    def test_failed_segment_selects_a_later_start(self) -> None:
        self.assertEqual(
            self.solution.canCompleteCircuit([2, 3, 4], [3, 4, 2]),
            2,
        )


if __name__ == "__main__":
    unittest.main()
