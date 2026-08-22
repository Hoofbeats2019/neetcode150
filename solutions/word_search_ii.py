"""Word Search II.

Created: 22 August 2026
Created by: Yanlong Su

Given a 2-D grid of characters ``board`` and a list of strings ``words``,
return every word that can be formed in the grid.

Each word must be formed by a path of horizontally or vertically neighboring
cells. The same cell may not be used more than once in one word.

Example 1:
    Input:
        board = [
            ["a", "b", "c", "d"],
            ["s", "a", "a", "t"],
            ["a", "c", "k", "e"],
            ["a", "c", "d", "n"],
        ]
        words = ["bat", "cat", "back", "backend", "stack"]
    Output: ["cat", "back", "backend"]

Example 2:
    Input:
        board = [["x", "o"], ["x", "o"]]
        words = ["xoxo"]
    Output: []

Constraints:
    1 <= len(board), len(board[i]) <= 12
    ``board[i][j]`` contains only lowercase English letters.
    1 <= len(words) <= 30,000
    1 <= len(words[i]) <= 10
    ``words[i]`` contains only lowercase English letters.
    All strings in ``words`` are unique.

Pseudocode:
    build a prefix tree containing every word
    store the complete word at each word's final trie node

    backtrack(row, column, trie_node):
        if the position is outside the board or already visited:
            return

        character = board[row][column]
        if character is not a child of trie_node:
            return

        next_node = trie_node.children[character]
        if next_node stores a complete word:
            append that word to the result
            clear the stored word so it cannot be added twice

        mark the position as visited
        search its horizontal and vertical neighbors from next_node
        remove the position from visited

    start backtracking from every board position
    return the result

Time complexity:
    O(S + rows * columns * 4^L) in the worst case, where S is the total
    number of characters in ``words`` and L is the longest word length.
Space complexity:
    O(S + L) auxiliary space for the trie, visited cells, and recursion stack,
    excluding the returned words.
"""

from __future__ import annotations

from typing import List


class TrieNode:
    """A trie node containing child links and an optional complete word."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word: str | None = None


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str],
    ) -> List[str]:
        """Return the words that can be formed by valid paths in ``board``."""
        root = TrieNode()

        # Reorganize the words into shared prefix paths.
        for word in words:
            current = root
            for character in word:
                if character not in current.children:
                    current.children[character] = TrieNode()
                current = current.children[character]
            current.word = word

        row_count = len(board)
        column_count = len(board[0])
        visited: set[tuple[int, int]] = set()
        result: list[str] = []

        def backtrack(row: int, column: int, node: TrieNode) -> None:
            """Search paths that continue from one board position."""
            is_outside_board = not (
                0 <= row < row_count and 0 <= column < column_count
            )
            if is_outside_board or (row, column) in visited:
                return

            character = board[row][column]

            # Prune when the current path is not a prefix of any word.
            if character not in node.children:
                return

            next_node = node.children[character]

            if next_node.word is not None:
                result.append(next_node.word)
                # A distinct input word should appear in the result only once.
                next_node.word = None

            visited.add((row, column))

            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for row_change, column_change in directions:
                backtrack(
                    row + row_change,
                    column + column_change,
                    next_node,
                )

            visited.remove((row, column))

        for row in range(row_count):
            for column in range(column_count):
                backtrack(row, column, root)

        return result


def example_board_1() -> list[list[str]]:
    """Return a fresh copy of the first example board."""
    return [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"],
    ]


def test_example_1() -> None:
    """Run the first worked example."""
    words = ["bat", "cat", "back", "backend", "stack"]
    actual = Solution().findWords(example_board_1(), words)
    assert set(actual) == {"cat", "back", "backend"}


def test_example_2() -> None:
    """Run the second worked example."""
    board = [["x", "o"], ["x", "o"]]
    assert Solution().findWords(board, ["xoxo"]) == []


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
