"""Valid Parenthesis String.

Created: 2 September 2026
Created by: Yanlong Su

You are given a string ``s`` containing only ``(``, ``)``, and ``*``. Return
``True`` when the string can be valid, otherwise return ``False``. A ``*`` may
represent ``(``, ``)``, or an empty string.

A valid string has matching parentheses, with every ``(`` appearing before its
matching ``)``.

Example 1:
    Input: s = "((**"
    Output: True
    Explanation: One ``*`` can be ``)`` and the other can be empty.

Example 2:
    Input: s = "(((*)"
    Output: False
    Explanation: At least two ``(`` remain unmatched for every choice of ``*``.

Constraints:
    1 <= len(s) <= 100
    s contains only ``(``, ``)``, and ``*``.

Approach:
    Track a range of possible numbers of unmatched opening parentheses while
    scanning left to right. ``low`` is the fewest possible unmatched opens and
    ``high`` is the most. An asterisk can lower the minimum by acting as ``)``,
    or raise the maximum by acting as ``(``. If ``high`` becomes negative, no
    possible interpretation can match the current closing parenthesis. Clamp
    ``low`` to zero because asterisk choices can be empty. The string is valid
    exactly when the minimum possible unmatched opens is zero at the end.

Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        """Return whether some interpretation of ``s`` is valid."""
        low = 0
        high = 0

        for character in s:
            if character == "(":
                low += 1
                high += 1
            elif character == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0


def test_example_1() -> None:
    """Run the first worked example."""
    expected = True
    actual = Solution().checkValidString("((**")
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = False
    actual = Solution().checkValidString("(((*)")
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
