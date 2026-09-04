"""Reverse Integer.

Created: 5 September 2026
Created by: Yanlong Su

Given a signed 32-bit integer ``x``, return ``x`` with its decimal digits
reversed. If the reversed value falls outside the signed 32-bit integer range
``[-2^31, 2^31 - 1]``, return ``0``.

Do not use integers outside the signed 32-bit integer range.

Example 1:
    Input: x = 1234
    Output: 4321

Example 2:
    Input: x = -1234
    Output: -4321

Example 3:
    Input: x = 1234236467
    Output: 0

Constraints:
    -2^31 <= x <= 2^31 - 1

Approach:
    Repeatedly remove the last decimal digit from ``x`` and append it to the
    result. Before each append, compare the result with the signed 32-bit
    boundary divided by ten. At the boundary, compare the final digit too, so
    an overflowing value is never constructed.

Time complexity: O(d), where d is the number of decimal digits
Space complexity: O(1)
"""


class Solution:
    def reverse(self, x: int) -> int:
        """Return ``x`` with its decimal digits reversed, or ``0`` on overflow."""
        minimum = -(2**31)
        maximum = 2**31 - 1
        minimum_tenth = minimum // 10 + 1
        reversed_number = 0

        while x != 0:
            remaining = x // 10
            digit = x % 10

            if x < 0 and digit != 0:
                remaining += 1
                digit -= 10

            x = remaining

            if reversed_number > maximum // 10 or (
                reversed_number == maximum // 10 and digit > 7
            ):
                return 0

            if reversed_number < minimum_tenth or (
                reversed_number == minimum_tenth and digit < -8
            ):
                return 0

            reversed_number = reversed_number * 10 + digit

        return reversed_number


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.reverse(1234) == 4321
    assert solution.reverse(-1234) == -4321
    assert solution.reverse(1234236467) == 0


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
