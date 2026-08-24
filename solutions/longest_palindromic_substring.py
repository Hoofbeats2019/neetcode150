"""Longest Palindromic Substring.

Created: 24 August 2026
Created by: Yanlong Su

Given a string ``s``, return its longest palindromic substring. A palindrome
reads the same forward and backward. If multiple palindromic substrings have
the same maximum length, return any one of them.

Example 1:
    Input: s = "ababd"
    Output: "bab"
    Explanation: Both "aba" and "bab" are valid answers.

Example 2:
    Input: s = "abbc"
    Output: "bb"

Constraints:
    1 <= len(s) <= 1000
    ``s`` contains only digits and English letters.

Pseudocode:
    longestPalindrome(s):
        set the best boundaries to the first character

        expand_from_center(left, right):
            while both boundaries are valid and their characters match:
                if this palindrome is longer than the best one:
                    update the best boundaries
                move both boundaries one position outward

        for each index in s:
            expand from that character for odd-length palindromes
            expand from the gap after it for even-length palindromes

        return the substring within the best boundaries

Time complexity: O(n^2)
Space complexity: O(1) auxiliary space
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return a longest palindromic substring of ``s``."""
        best_left = 0
        best_right = 0

        def expand_from_center(left: int, right: int) -> None:
            """Expand while the inclusive interval remains a palindrome."""
            nonlocal best_left, best_right

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                current_length = right - left + 1
                best_length = best_right - best_left + 1

                if current_length > best_length:
                    best_left = left
                    best_right = right

                left -= 1
                right += 1

        for center in range(len(s)):
            expand_from_center(center, center)
            expand_from_center(center, center + 1)

        return s[best_left : best_right + 1]


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().longestPalindrome("ababd") in {"aba", "bab"}


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().longestPalindrome("abbc") == "bb"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
