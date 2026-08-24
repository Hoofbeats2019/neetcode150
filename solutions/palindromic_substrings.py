"""Palindromic Substrings.

Created: 24 August 2026
Created by: Yanlong Su

Given a string ``s``, return the number of substrings within ``s`` that are
palindromes. A palindrome reads the same forward and backward. Substrings at
different positions are counted separately, even when their contents match.

Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: "a", "b", and "c".

Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: "a", "a", "a", "aa", "aa", and "aaa".

Constraints:
    1 <= len(s) <= 1000
    ``s`` contains only lowercase English letters.

Pseudocode:
    countSubstrings(s):
        set the palindrome count to zero

        expand_from_center(left, right):
            while both boundaries are valid and their characters match:
                increment the palindrome count
                move both boundaries one position outward

        for each index in s:
            expand from that character for odd-length palindromes
            expand from the gap after it for even-length palindromes

        return the palindrome count

Time complexity: O(n^2)
Space complexity: O(1) auxiliary space
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """Return the number of palindromic substrings in ``s``."""
        palindrome_count = 0

        def expand_from_center(left: int, right: int) -> None:
            """Count palindromes while expanding around one center."""
            nonlocal palindrome_count

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                palindrome_count += 1
                left -= 1
                right += 1

        for center in range(len(s)):
            expand_from_center(center, center)
            expand_from_center(center, center + 1)

        return palindrome_count


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().countSubstrings("abc") == 3


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().countSubstrings("aaa") == 6


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
