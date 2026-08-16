"""Palindrome Partitioning.

Created: 16 August 2026
Created by: Yanlong Su

Given a string ``s``, split it into substrings so that every substring in the
partition is a palindrome. Return every possible palindrome partition of
``s``. The partitions may be returned in any order.

A palindrome reads the same forward and backward.

Example 1:
    Input: s = "aab"
    Output: [["a", "a", "b"], ["aa", "b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    1 <= len(s) <= 20
    ``s`` contains only lowercase English letters.

Pseudocode:
    partition(s):
        create an empty result list
        create an empty current partition
        create an empty palindrome cache

        is_palindrome(left, right):
            if left is greater than or equal to right:
                return True

            if (left, right) is cached:
                return the cached result

            cache whether the outer characters match and the inner substring
            is a palindrome
            return the cached result

        backtrack(start):
            if start equals the length of s:
                add a copy of the current partition to result
                return

            for right from start through the last index of s:
                if s[start:right + 1] is not a palindrome:
                    continue

                add s[start:right + 1] to the current partition
                backtrack(right + 1)
                remove the last substring from the current partition

        backtrack(0)
        return result

Time complexity: O(n * 2^n)
Space complexity: O(n^2) auxiliary; O(n * 2^n) including returned partitions
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """Return every partition of s containing only palindromes."""
        result: list[list[str]] = []
        current_partition: list[str] = []
        palindrome_cache: dict[tuple[int, int], bool] = {}

        def is_palindrome(left: int, right: int) -> bool:
            """Return whether the inclusive substring s[left:right + 1] is a palindrome."""
            if left >= right:
                return True

            boundaries = (left, right)
            if boundaries in palindrome_cache:
                return palindrome_cache[boundaries]

            palindrome_cache[boundaries] = (
                s[left] == s[right]
                and is_palindrome(left + 1, right - 1)
            )
            return palindrome_cache[boundaries]

        def backtrack(start: int) -> None:
            """Choose the next palindrome beginning at start."""
            # VALID RESULT CHECK: every character belongs to a palindrome.
            if start == len(s):
                result.append(current_partition.copy())
                return

            # CHOICES: try every possible ending for the next substring.
            for right in range(start, len(s)):
                if not is_palindrome(start, right):
                    # A longer substring may still become a palindrome.
                    continue

                # MAKE THE CHOICE.
                current_partition.append(s[start : right + 1])

                # EXPLORE the unpartitioned suffix.
                backtrack(right + 1)

                # UNDO THE CHOICE before trying a longer substring.
                current_partition.pop()

        backtrack(0)
        return result


def normalize(partitions: list[list[str]]) -> list[tuple[str, ...]]:
    """Normalize partition ordering for the executable examples."""
    return sorted(tuple(partition) for partition in partitions)


def test_example_1() -> None:
    actual = Solution().partition("aab")
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().partition("a")
    assert actual == [["a"]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
