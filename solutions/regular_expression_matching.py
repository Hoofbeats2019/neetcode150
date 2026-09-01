"""Regular Expression Matching.

Created: 1 September 2026
Created by: Yanlong Su

Given an input string ``s`` of lowercase English letters and a pattern ``p``
containing lowercase English letters, ``.`` and ``*``, return whether the
pattern matches the entire string.

``.`` matches any single character. ``*`` matches zero or more occurrences of
the preceding character or ``.``.

Example 1:
    Input: s = "aa", p = ".b"
    Output: False
    Explanation: The second pattern character cannot match the second input
        character.

Example 2:
    Input: s = "nnn", p = "n*"
    Output: True
    Explanation: ``n*`` matches all three ``n`` characters.

Example 3:
    Input: s = "xyz", p = ".*z"
    Output: True
    Explanation: ``.*`` matches "xy", then ``z`` matches the final character.

Constraints:
    1 <= len(s) <= 20
    1 <= len(p) <= 20
    Every ``*`` is preceded by a lowercase English letter or ``.``.

Pseudocode:
    isMatch(s, p):
        create an empty memo

        dfs(i, j):
            if the pattern is exhausted:
                return whether the string is also exhausted
            if (i, j) is memoized:
                return its result

            first_match = s[i] matches p[j], including ``.``

            if p[j + 1] is ``*``:
                skip the preceding pattern character and ``*``
                or, when first_match, consume s[i] and keep the same pattern
            otherwise, when first_match, consume one character from both

            memoize and return the result

        return dfs(0, 0)

Time complexity: O(len(s) * len(p))
Space complexity: O(len(s) * len(p))
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Return whether ``p`` matches all of ``s``."""
        memo: dict[tuple[int, int], bool] = {}

        def dfs(string_index: int, pattern_index: int) -> bool:
            if pattern_index == len(p):
                return string_index == len(s)

            state = (string_index, pattern_index)

            if state in memo:
                return memo[state]

            first_match = (
                string_index < len(s)
                and (p[pattern_index] == s[string_index] or p[pattern_index] == ".")
            )

            if pattern_index + 1 < len(p) and p[pattern_index + 1] == "*":
                matches = dfs(string_index, pattern_index + 2) or (
                    first_match and dfs(string_index + 1, pattern_index)
                )
            else:
                matches = first_match and dfs(string_index + 1, pattern_index + 1)

            memo[state] = matches
            return matches

        return dfs(0, 0)


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().isMatch("aa", ".b") is False


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().isMatch("nnn", "n*") is True


def test_example_3() -> None:
    """Run the third worked example."""
    assert Solution().isMatch("xyz", ".*z") is True


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
