"""Valid Anagram.

Return whether two lowercase strings contain the same characters with the
same frequencies.

Examples:
    isAnagram("anagram", "nagaram") -> True
    isAnagram("rat", "car") -> False
"""

from collections import Counter


class Solution:
    """Compare character frequencies in the two strings."""

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def test_worked_examples() -> None:
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") is True
    assert solution.isAnagram("rat", "car") is False


if __name__ == "__main__":
    test_worked_examples()
    print("The worked examples passed.")
