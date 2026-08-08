"""Time Based Key-Value Store.

Created: 5 August 2026
Created by: Yanlong Su

Store multiple values for each key at different timestamps and retrieve the
value associated with the greatest stored timestamp that does not exceed the
requested timestamp.

Timestamps passed to ``set`` are strictly increasing, so appending each value
keeps its key's entries sorted. This makes ``set`` O(1) amortized and allows
``get`` to use an O(log n) binary search.
"""


class TimeMap:
    def __init__(self) -> None:
        self.store: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            middle = left + (right - left) // 2
            value, stored_timestamp = values[middle]

            if stored_timestamp <= timestamp:
                result = value
                left = middle + 1
            else:
                right = middle - 1

        return result
