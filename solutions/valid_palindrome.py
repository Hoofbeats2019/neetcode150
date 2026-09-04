"""Valid Palindrome.

Return whether a string reads the same forward and backward after ignoring
non-alphanumeric characters and letter case.
"""


class Solution:
    """Compare valid characters from both ends of the string."""

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")
    print("The worked example passed.")
