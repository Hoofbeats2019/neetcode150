import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.top_k_frequent_elements import Solution


class TestTopKFrequentElements(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example(self) -> None:
        self.assertEqual(set(self.solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)), {1, 2})

    def test_one_value(self) -> None:
        self.assertEqual(self.solution.topKFrequent([1], 1), [1])

    def test_negative_values(self) -> None:
        self.assertEqual(set(self.solution.topKFrequent([-1, -1, 2, 2, 2], 1)), {2})


if __name__ == "__main__":
    unittest.main()
