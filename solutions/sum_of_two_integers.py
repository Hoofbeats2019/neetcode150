"""Sum of Two Integers.

Created: 5 September 2026
Created by: Yanlong Su

Given two integers ``a`` and ``b``, return their sum without using the ``+``
or ``-`` operators.

Example 1:
    Input: a = 1, b = 1
    Output: 2

Example 2:
    Input: a = 4, b = 7
    Output: 11

Constraints:
    -1000 <= a, b <= 1000

Approach:
    XOR computes the partial sum without carry bits. AND identifies the carry
    bits, which are shifted left before the next iteration. Restrict each
    intermediate result to 32 bits so negative Python integers behave like
    signed 32-bit values during the bitwise operations.

Time complexity: O(1), because at most 32 carry positions are processed
Space complexity: O(1)
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """Return the sum of ``a`` and ``b`` using bitwise operations."""
        mask = 0xFFFFFFFF
        signed_bit = 1 << 31

        while b != 0:
            partial_sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = partial_sum
            b = carry

        return a if a < signed_bit else ~(a ^ mask)


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.getSum(1, 1) == 2
    assert solution.getSum(4, 7) == 11


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
