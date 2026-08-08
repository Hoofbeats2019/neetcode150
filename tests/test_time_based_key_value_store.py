import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.time_based_key_value_store import TimeMap


class TestTimeMap(unittest.TestCase):
    def setUp(self) -> None:
        self.time_map = TimeMap()

    def test_exact_timestamp(self) -> None:
        self.time_map.set("alice", "happy", 1)
        self.assertEqual(self.time_map.get("alice", 1), "happy")

    def test_latest_value_before_timestamp(self) -> None:
        self.time_map.set("alice", "happy", 1)
        self.assertEqual(self.time_map.get("alice", 2), "happy")

    def test_latest_of_multiple_values(self) -> None:
        self.time_map.set("alice", "happy", 1)
        self.time_map.set("alice", "sad", 3)
        self.assertEqual(self.time_map.get("alice", 3), "sad")
        self.assertEqual(self.time_map.get("alice", 10), "sad")

    def test_timestamp_before_first_value(self) -> None:
        self.time_map.set("alice", "happy", 2)
        self.assertEqual(self.time_map.get("alice", 1), "")

    def test_missing_key(self) -> None:
        self.assertEqual(self.time_map.get("unknown", 5), "")

    def test_keys_are_independent(self) -> None:
        self.time_map.set("alice", "happy", 1)
        self.time_map.set("bob", "calm", 2)
        self.assertEqual(self.time_map.get("alice", 2), "happy")
        self.assertEqual(self.time_map.get("bob", 2), "calm")


if __name__ == "__main__":
    unittest.main()
