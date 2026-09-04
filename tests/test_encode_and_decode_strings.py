import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solutions.encode_and_decode_strings import Solution


class TestEncodeAndDecodeStrings(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_round_trip(self) -> None:
        values = ["neet", "code", "love", "you"]
        self.assertEqual(self.solution.decode(self.solution.encode(values)), values)

    def test_empty_strings_and_delimiters(self) -> None:
        values = ["", "#", "12#abc", ""]
        self.assertEqual(self.solution.decode(self.solution.encode(values)), values)

    def test_empty_list(self) -> None:
        self.assertEqual(self.solution.decode(self.solution.encode([])), [])


if __name__ == "__main__":
    unittest.main()
