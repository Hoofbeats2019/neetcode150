"""Design Add and Search Word Data Structure.

Created: 22 August 2026
Created by: Yanlong Su

Design a data structure that supports adding new words and searching for
existing words.

Implement the ``WordDictionary`` class:

* ``addWord(word)`` adds ``word`` to the data structure.
* ``search(word)`` returns whether a stored word matches ``word``. A dot
  (``.``) may match any single letter.

Example:
    Input:
        ["WordDictionary", "addWord", "addWord", "addWord", "search",
         "search", "search", "search"]
        [[], ["day"], ["bay"], ["may"], ["say"], ["day"], [".ay"],
         ["b.."]]
    Output:
        [null, null, null, null, false, true, true, true]

Constraints:
    1 <= word.length <= 25
    Words added contain only lowercase English letters.
    Search queries contain dots or lowercase English letters.
    A search query contains at most two dots.
    At most 10,000 calls are made to ``addWord`` and ``search``.

Pseudocode:
    Node:
        children = empty dictionary mapping characters to child nodes
        is_end = false

    addWord(word):
        current = root
        for each character in word:
            create the missing child when necessary
            move current to that child
        mark current as the end of a word

    search(word):
        dfs(node, index):
            if index equals the length of word:
                return node.is_end

            character = word[index]
            if character is not a dot:
                return false if its child does not exist
                otherwise recurse into that child

            for every child:
                return true if recursion from that child succeeds
            return false

        return dfs(root, 0)

Time complexity:
    ``addWord`` is O(L). ``search`` is O(26^d * L) in the worst case, where
    L is the query length and d is its number of dots.
Space complexity:
    O(C) for C inserted characters, plus O(L) recursive search space.
"""


class _Node:
    """A trie node with child links and an end-of-word marker."""

    def __init__(self) -> None:
        self.children: dict[str, "_Node"] = {}
        self.is_end = False


class WordDictionary:
    """Store words and support exact or dot-wildcard searches."""

    def __init__(self) -> None:
        self.root = _Node()

    def addWord(self, word: str) -> None:
        """Add ``word`` to the data structure."""
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = _Node()
            current = current.children[character]

        current.is_end = True

    def search(self, word: str) -> bool:
        """Return whether a stored word matches ``word``."""

        def dfs(node: _Node, index: int) -> bool:
            if index == len(word):
                return node.is_end

            character = word[index]

            if character != ".":
                if character not in node.children:
                    return False
                return dfs(node.children[character], index + 1)

            for child in node.children.values():
                if dfs(child, index + 1):
                    return True

            return False

        return dfs(self.root, 0)


def test_example_1() -> None:
    words = WordDictionary()
    words.addWord("day")
    words.addWord("bay")
    words.addWord("may")
    assert words.search("say") is False
    assert words.search("day") is True
    assert words.search(".ay") is True
    assert words.search("b..") is True


if __name__ == "__main__":
    test_example_1()
    print("Example test passed.")
