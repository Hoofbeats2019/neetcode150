"""Word Ladder.

Created: 23 August 2026
Created by: Yanlong Su

You are given two words, ``beginWord`` and ``endWord``, and a list of words
``wordList``. All words have the same length, contain only lowercase English
letters, and are distinct.

Transform ``beginWord`` into ``endWord`` using these rules:

- A word may be transformed into any word in ``wordList`` that differs from
  it at exactly one character position.
- The transformation may be repeated as many times as needed.

Return the minimum number of words in a transformation sequence that reaches
``endWord``. Return ``0`` if no such sequence exists.

Example 1:
    Input:
        beginWord = "cat"
        endWord = "sag"
        wordList = ["bat", "bag", "sag", "dag", "dot"]
    Output: 4
    Explanation:
        The sequence is "cat" -> "bat" -> "bag" -> "sag".

Example 2:
    Input:
        beginWord = "cat"
        endWord = "sag"
        wordList = ["bat", "bag", "sat", "dag", "dot"]
    Output: 0
    Explanation:
        No sequence can reach "sag" because it is not in ``wordList``.

Constraints:
    1 <= len(beginWord) <= 10
    1 <= len(wordList) <= 100

Pseudocode:
    ladderLength(beginWord, endWord, wordList):
        if endWord is not in wordList:
            return 0

        create a words list containing beginWord and every other listed word
        create an adjacency matrix with one row and column per word

        for every pair of words:
            count their character differences
            if exactly one character differs:
                connect the pair in both directions

        add beginWord's index and edge distance 0 to a queue
        mark beginWord's index as visited

        while the queue is not empty:
            remove the next node and its edge distance
            if the node is endWord:
                return the edge distance plus 1

            add every connected unvisited node with distance plus 1
            mark each added node as visited

        return 0

Time complexity: O(n^2 * L)
Space complexity: O(n^2)
"""

from collections import deque
from typing import List


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str],
    ) -> int:
        """Return the minimum sequence length needed to reach endWord."""
        if endWord not in wordList:
            return 0

        # beginWord is the source node even when it is not in wordList.
        words = [beginWord]
        for word in wordList:
            if word != beginWord:
                words.append(word)

        word_count = len(words)
        graph = [
            [0 for _ in range(word_count)]
            for _ in range(word_count)
        ]

        # Connect each pair that differs at exactly one character position.
        for first_index in range(word_count):
            for second_index in range(first_index + 1, word_count):
                differences = 0

                for position in range(len(words[first_index])):
                    if (
                        words[first_index][position]
                        != words[second_index][position]
                    ):
                        differences += 1

                if differences == 1:
                    graph[first_index][second_index] = 1
                    graph[second_index][first_index] = 1

        source = 0
        destination = words.index(endWord)
        queue: deque[tuple[int, int]] = deque([(source, 0)])
        visited = {source}

        while queue:
            node, edge_distance = queue.popleft()

            if node == destination:
                return edge_distance + 1

            for neighbor in range(word_count):
                if graph[node][neighbor] == 0:
                    continue

                if neighbor in visited:
                    continue

                visited.add(neighbor)
                queue.append((neighbor, edge_distance + 1))

        return 0


def test_example_1() -> None:
    """Run the first worked example."""
    word_list = ["bat", "bag", "sag", "dag", "dot"]
    assert Solution().ladderLength("cat", "sag", word_list) == 4


def test_example_2() -> None:
    """Run the second worked example."""
    word_list = ["bat", "bag", "sat", "dag", "dot"]
    assert Solution().ladderLength("cat", "sag", word_list) == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
