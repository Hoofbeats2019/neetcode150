"""Non-Cyclical Number.

Created: 4 September 2026
Created by: Yanlong Su

Given a positive integer, repeatedly replace it with the sum of the squares of
its digits. A number is non-cyclical if this process reaches ``1``. Return
``True`` for a non-cyclical number; otherwise, return ``False`` when the
process enters a cycle that does not contain ``1``.

Example 1:
    Input: n = 100
    Output: True
    Explanation: 1² + 0² + 0² = 1

Example 2:
    Input: n = 101
    Output: False
    Explanation: 101 becomes 2, 4, 16, 37, 58, 89, 145, 42, 20, then 4 again.

Constraints:
    1 <= n <= 1000

Approach:
    Treat each digit-square sum as the next value in a sequence. Move ``slow``
    forward by one transformation and ``fast`` forward by two. If either value
    reaches ``1``, the number is non-cyclical. If they become equal first,
    they are inside a cycle that does not contain ``1``.

Time complexity: O(log n)
Space complexity: O(1)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """Return whether repeatedly transforming ``n`` eventually reaches 1."""
        slow = n
        fast = n

        while True:
            slow = self._nextNumber(slow)
            fast = self._nextNumber(self._nextNumber(fast))

            if slow == 1 or fast == 1:
                return True

            if slow == fast:
                return False

    def _nextNumber(self, n: int) -> int:
        """Return the sum of the squares of the digits in ``n``."""
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.isHappy(100) is True
    assert solution.isHappy(101) is False


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
