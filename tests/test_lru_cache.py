"""Unit tests for the LRU cache.

Test pseudocode:
    for the worked example:
        insert and access keys in the given order
        verify that the least recently used key is evicted

    for each recency rule:
        fill the cache
        use a key with get or put
        insert another key
        verify that the untouched least-recent key is evicted

    for edge cases:
        verify missing keys
        verify capacity one
        verify zero is accepted as a key and value
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_example(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        cache.put(2, 20)
        cache.put(3, 30)
        self.assertEqual(cache.get(2), 20)
        self.assertEqual(cache.get(1), -1)

    def test_get_marks_key_as_most_recently_used(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)

        self.assertEqual(cache.get(1), 10)
        cache.put(3, 30)

        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 30)

    def test_put_updates_value_and_recency(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(1, 100)
        cache.put(3, 30)

        self.assertEqual(cache.get(1), 100)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 30)

    def test_capacity_one(self) -> None:
        cache = LRUCache(1)
        cache.put(1, 10)
        cache.put(2, 20)

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 20)

    def test_missing_key(self) -> None:
        cache = LRUCache(2)
        self.assertEqual(cache.get(99), -1)

    def test_zero_key_and_value(self) -> None:
        cache = LRUCache(1)
        cache.put(0, 0)
        self.assertEqual(cache.get(0), 0)


if __name__ == "__main__":
    unittest.main()
