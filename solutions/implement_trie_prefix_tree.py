"""Implement Trie (Prefix Tree).

Created: 22 August 2026
Created by: Yanlong Su

A prefix tree, also known as a trie, efficiently stores and retrieves strings
by sharing paths between words with the same prefix.

Implement the ``PrefixTree`` class:

* ``PrefixTree()`` initializes an empty prefix tree.
* ``insert(word)`` inserts ``word`` into the prefix tree.
* ``search(word)`` returns whether ``word`` was previously inserted.
* ``startsWith(prefix)`` returns whether an inserted word starts with
  ``prefix``.

Example:
    Input:
        ["Trie", "insert", "dog", "search", "dog", "search", "do",
         "startsWith", "do", "insert", "do", "search", "do"]
    Output:
        [null, null, true, false, true, null, true]

Executable example:
    >>> prefix_tree = PrefixTree()
    >>> prefix_tree.insert("dog")
    >>> prefix_tree.search("dog")
    True
    >>> prefix_tree.search("do")
    False
    >>> prefix_tree.startsWith("do")
    True
    >>> prefix_tree.insert("do")
    >>> prefix_tree.search("do")
    True

Constraints:
    1 <= word.length, prefix.length <= 1000
    ``word`` and ``prefix`` contain only lowercase English letters.

Pseudocode:
    Node:
        children = empty dictionary mapping characters to child nodes
        is_end = false

    PrefixTree:
        root = new Node

    insert(word):
        current = root
        for each character in word:
            if character is not in current.children:
                create and store a new child node for character
            move current to that child
        mark current as the end of a word

    search(word):
        current = root
        for each character in word:
            if character is not in current.children:
                return false
            move current to that child
        return whether current is marked as the end of a word

    startsWith(prefix):
        current = root
        for each character in prefix:
            if character is not in current.children:
                return false
            move current to that child
        return true
"""

from __future__ import annotations


class Node:
    """A trie node with character-to-child links and a word-end marker."""

    def __init__(self) -> None:
        self.children: dict[str, Node] = {}
        self.is_end = False


class PrefixTree:
    """Store words in a tree of shared character prefixes."""

    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = Node()
            current = current.children[character]

        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root

        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]

        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]

        return True


def test_example_1() -> None:
    prefix_tree = PrefixTree()
    prefix_tree.insert("dog")
    assert prefix_tree.search("dog") is True
    assert prefix_tree.search("do") is False
    assert prefix_tree.startsWith("do") is True
    prefix_tree.insert("do")
    assert prefix_tree.search("do") is True


if __name__ == "__main__":
    test_example_1()
    print("Example test passed.")
