"""Pow(x, n).

Created: 4 September 2026
Created by: Yanlong Su

Implement ``myPow(x, n)``, which returns ``x`` raised to the integer power
``n``. Built-in exponentiation functions may not be used.

Example 1:
    Input: x = 2.00000, n = 5
    Output: 32.00000

Example 2:
    Input: x = 1.10000, n = 10
    Output: 2.59374

Example 3:
    Input: x = 2.00000, n = -3
    Output: 0.12500

Constraints:
    -100.0 < x < 100.0
    -2**31 <= n <= 2**31 - 1
    n is an integer.
    Either x is not zero or n > 0.
    -10**4 <= x**n <= 10**4

Approach:
    For a non-negative exponent, recursively calculate the power for half the
    exponent, then square it. When the exponent is odd, multiply by ``x`` one
    additional time. For a negative exponent, calculate the corresponding
    positive power and return its reciprocal.

Time complexity: O(log |n|)
Space complexity: O(log |n|)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Return ``x`` raised to the integer power ``n``."""
        if n < 0:
            return 1 / self._power(x, -n)

        return self._power(x, n)

    def _power(self, x: float, n: int) -> float:
        """Return ``x**n`` for a non-negative integer ``n``."""
        if n == 0:
            return 1

        half_power = self._power(x, n // 2)
        result = half_power * half_power

        if n % 2 == 1:
            result *= x

        return result


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.myPow(2.0, 5) == 32.0
    assert round(solution.myPow(1.1, 10), 5) == 2.59374
    assert solution.myPow(2.0, -3) == 0.125


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
