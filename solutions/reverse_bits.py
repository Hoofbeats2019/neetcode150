"""Reverse Bits.

Created: 5 September 2026
Created by: Yanlong Su

Given a 32-bit unsigned integer ``n``, reverse the bits in its binary
representation and return the resulting unsigned integer.

Example 1:
    Input: n = 21 (00000000000000000000000000010101)
    Output: 2818572288 (10101000000000000000000000000000)
    Explanation: Reversing the 32 bits of 21 moves its set bits to positions
    31, 29, and 27.

Example 2:
    Input: n = 43261596 (00000010100101000001111010011100)
    Output: 964176192 (00111001011110000010100101000000)

Constraints:
    0 <= n <= 2^32 - 1

Approach:
    Inspect each bit at position ``i`` with ``(n >> i) & 1``. When it is set,
    set bit ``31 - i`` in the result. This places every bit at its reversed
    position.

Time complexity: O(1), because exactly 32 bits are inspected
Space complexity: O(1)
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        """Return ``n`` with its 32 bits reversed."""
        result = 0

        for i in range(32):
            bit = (n >> i) & 1

            if bit == 1:
                result |= 1 << (31 - i)

        return result


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.reverseBits(21) == 2818572288
    assert solution.reverseBits(43261596) == 964176192


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
