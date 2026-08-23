"""Alien Dictionary.

Created: 23 August 2026
Created by: Yanlong Su

An alien language uses the English alphabet, but the order of its letters is
unknown. The strings in ``words`` are claimed to be sorted lexicographically
according to that unknown order.

Return every unique letter appearing in ``words`` in one valid alien-alphabet
order. If the words cannot correspond to any letter order, return an empty
string. When multiple valid orders exist, return any one of them.

A word is lexicographically smaller when its first differing letter is smaller,
or when it is a shorter prefix of the other word.

Example 1:
    Input: words = ["z", "o"]
    Output: "zo"
    Explanation: The word order shows that ``z`` comes before ``o``.

Example 2:
    Input: words = ["hrn", "hrf", "er", "enn", "rfnn"]
    Output: "hernf"
    Explanation: The neighboring words establish ``n < f``, ``h < e``,
    ``r < n``, and ``e < r``.

Example 3:
    Input: words = ["abc", "ab"]
    Output: ""
    Explanation: A longer word cannot appear before its own prefix.

Constraints:
    1 <= len(words) <= 100
    1 <= len(words[i]) <= 100
    words[i] contains only lowercase English letters.

Pseudocode:
    foreignDictionary(words):
        create one graph node for every unique letter
        compare every word with its next neighbor
        if the first word is longer and the second is its prefix, return ""
        add an edge between the first different letters and stop comparing

        run DFS from every unvisited letter
        return "" if DFS reaches a letter on the current path
        append each letter after all of its neighbors are processed

        reverse the DFS postorder and return it as a string

Time complexity: O(C + V + E), where C is the total number of input characters
Space complexity: O(V + E)
"""

from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """Return a valid alien letter order, or an empty string."""
        adjacency_list: dict[str, set[str]] = {}

        for word in words:
            for character in word:
                adjacency_list.setdefault(character, set())

        for index in range(len(words) - 1):
            first_word = words[index]
            second_word = words[index + 1]
            shared_length = min(len(first_word), len(second_word))

            if (
                len(first_word) > len(second_word)
                and first_word[:shared_length]
                == second_word[:shared_length]
            ):
                return ""

            for character_index in range(shared_length):
                first_character = first_word[character_index]
                second_character = second_word[character_index]

                if first_character != second_character:
                    adjacency_list[first_character].add(second_character)
                    break

        unvisited = 0
        visiting = 1
        visited = 2
        states = {
            character: unvisited for character in adjacency_list
        }
        order: list[str] = []

        def dfs(character: str) -> bool:
            if states[character] == visiting:
                return False

            if states[character] == visited:
                return True

            states[character] = visiting

            for next_character in adjacency_list[character]:
                if not dfs(next_character):
                    return False

            states[character] = visited
            order.append(character)
            return True

        for character in adjacency_list:
            if states[character] == unvisited and not dfs(character):
                return ""

        order.reverse()
        return "".join(order)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().foreignDictionary(["z", "o"]) == "zo"


def test_example_2() -> None:
    """Run the second worked example."""
    words = ["hrn", "hrf", "er", "enn", "rfnn"]
    assert Solution().foreignDictionary(words) == "hernf"


def test_example_3() -> None:
    """Run the invalid-prefix worked example."""
    assert Solution().foreignDictionary(["abc", "ab"]) == ""


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
