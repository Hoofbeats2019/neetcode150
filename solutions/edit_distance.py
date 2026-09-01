"""Edit Distance.

Created: 1 September 2026
Created by: Yanlong Su

Given two strings ``word1`` and ``word2``, return the minimum number of
insertions, deletions, and replacements needed to make ``word1`` equal to
``word2``.

Example 1:
    Input: word1 = "monkeys", word2 = "money"
    Output: 2
    Explanation: Remove "s", then replace "k" with "y".

Example 2:
    Input: word1 = "neatcdee", word2 = "neetcode"
    Output: 3
    Explanation: Replace "a" with "e", remove the final "e", then insert "o".

Constraints:
    0 <= len(word1), len(word2) <= 100
    word1 and word2 consist only of lowercase English letters.

Pseudocode:
    minDistance(word1, word2):
        create an empty memo

        dfs(i, j):
            if i reaches the end of word1:
                return the number of remaining characters in word2
            if j reaches the end of word2:
                return the number of remaining characters in word1
            if (i, j) is memoized:
                return its result

            if word1[i] equals word2[j]:
                return dfs(i + 1, j + 1)

            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)
            memoize and return the smallest operation count

        return dfs(0, 0)

Time complexity: O(len(word1) * len(word2))
Space complexity: O(len(word1) * len(word2))
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the fewest edits needed to transform ``word1`` into ``word2``."""
        memo: dict[tuple[int, int], int] = {}

        def dfs(index1: int, index2: int) -> int:
            if index1 == len(word1):
                return len(word2) - index2

            if index2 == len(word2):
                return len(word1) - index1

            state = (index1, index2)

            if state in memo:
                return memo[state]

            if word1[index1] == word2[index2]:
                result = dfs(index1 + 1, index2 + 1)
            else:
                insert_character = 1 + dfs(index1, index2 + 1)
                delete_character = 1 + dfs(index1 + 1, index2)
                replace_character = 1 + dfs(index1 + 1, index2 + 1)
                result = min(insert_character, delete_character, replace_character)

            memo[state] = result
            return result

        return dfs(0, 0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().minDistance("monkeys", "money") == 2


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().minDistance("neatcdee", "neetcode") == 3


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("All example tests passed.")
