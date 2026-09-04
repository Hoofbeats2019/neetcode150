"""Number of 1 Bits.

Created: 5 September 2026
Created by: Yanlong Su

You are given an unsigned integer ``n``. Return the number of ``1`` bits in
its binary representation.

Example 1:
    Input: n = 23
    Output: 4
    Explanation: The binary representation of 23 is 10111, which contains
    four 1 bits.

Example 2:
    Input: n = 2147483645
    Output: 30
    Explanation: The binary representation of 2147483645 is
    1111111111111111111111111111101, which contains thirty 1 bits.

Constraints:
    0 <= n <= 2^31 - 1

Approach:
    Inspect the rightmost bit with ``n & 1`` and add it to a counter. Shift
    ``n`` right by one position to inspect the next bit. Repeat until ``n``
    becomes zero.

Time complexity: O(log n)
Space complexity: O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """Return the number of 1 bits in ``n``."""
        count = 0

        while n > 0:
            count += n & 1
            n >>= 1

        return count


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.hammingWeight(23) == 4
    assert solution.hammingWeight(2147483645) == 30


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
