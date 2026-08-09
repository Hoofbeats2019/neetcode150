"""LRU Cache.

Created: 9 August 2026
Created by: Yanlong Su

Implement a Least Recently Used (LRU) cache with these operations:

* ``LRUCache(capacity)`` creates a cache with the given capacity.
* ``get(key)`` returns the key's value, or ``-1`` when the key is absent.
* ``put(key, value)`` inserts or updates a key and evicts the least recently
  used key when the cache exceeds its capacity.

A successful ``get`` and every ``put`` mark a key as recently used. Both
operations must run in O(1) average time.

Example:
    Input:
        ["LRUCache", [2], "put", [1, 10], "get", [1], "put", [2, 20],
         "put", [3, 30], "get", [2], "get", [1]]
    Output:
        [null, null, 10, null, null, 20, -1]

Executable example:
    >>> cache = LRUCache(2)
    >>> cache.put(1, 10)
    >>> cache.get(1)
    10
    >>> cache.put(2, 20)
    >>> cache.put(3, 30)
    >>> cache.get(2)
    20
    >>> cache.get(1)
    -1

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls are made to ``get`` and ``put``.

Pseudocode:
    Node(key, value):
        store key, value, previous pointer, and next pointer

    LRUCache(capacity):
        store capacity
        create an empty dictionary mapping keys to nodes
        connect dummy head and tail nodes
        head.next represents the LRU node
        tail.previous represents the MRU node

    remove(node):
        connect node.previous directly to node.next

    add_to_mru(node):
        insert node immediately before the dummy tail

    move_to_mru(node):
        remove node from its current position
        add node immediately before the dummy tail

    get(key):
        if key is absent, return -1
        find its node through the dictionary
        move the node to the MRU position
        return the node's value

    put(key, value):
        if key exists:
            update its node's value
            move the node to the MRU position
            return
        create a new node
        map the key to the node
        add the node to the MRU position
        if the number of keys exceeds capacity:
            remove the node immediately after head
            delete that node's key from the dictionary
"""

from __future__ import annotations


class _Node:
    """A key-value entry in the cache's doubly linked list."""

    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, _Node] = {}

        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: _Node) -> None:
        previous_node = node.prev
        next_node = node.next

        if previous_node is None or next_node is None:
            raise ValueError("Cannot remove a node outside the cache list")

        previous_node.next = next_node
        next_node.prev = previous_node

    def _add_to_mru(self, node: _Node) -> None:
        previous_mru = self.tail.prev

        if previous_mru is None:
            raise ValueError("Cache list is not initialized")

        previous_mru.next = node
        node.prev = previous_mru
        node.next = self.tail
        self.tail.prev = node

    def _move_to_mru(self, node: _Node) -> None:
        self._remove(node)
        self._add_to_mru(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_mru(node)
            return

        new_node = _Node(key, value)
        self.cache[key] = new_node
        self._add_to_mru(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.head.next

            if lru_node is None or lru_node is self.tail:
                raise ValueError("Cache list does not contain an LRU node")

            self._remove(lru_node)
            del self.cache[lru_node.key]


def test_example_1() -> None:
    cache = LRUCache(2)
    cache.put(1, 10)
    assert cache.get(1) == 10
    cache.put(2, 20)
    cache.put(3, 30)
    assert cache.get(2) == 20
    assert cache.get(1) == -1


if __name__ == "__main__":
    test_example_1()
    print("Example test passed.")
