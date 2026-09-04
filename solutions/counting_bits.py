"""Counting Bits.

Created: 5 September 2026
Created by: Yanlong Su

Given an integer ``n``, return an array where the value at each index ``i``
is the number of ``1`` bits in the binary representation of ``i`` for every
integer in the range ``[0, n]``.

Example 1:
    Input: n = 4
    Output: [0, 1, 1, 2, 1]
    Explanation: The binary representations are 0, 1, 10, 11, and 100.

Constraints:
    0 <= n <= 1000

Approach:
    For each number ``i``, ``i // 2`` removes its final binary digit and
    ``i % 2`` is that final digit. Therefore, the number of 1 bits in ``i``
    is the stored count for ``i // 2`` plus ``i % 2``.

Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        """Return the number of 1 bits for every integer from 0 through ``n``."""
        output = [0] * (n + 1)

        for i in range(1, n + 1):
            output[i] = output[i // 2] + (i % 2)

        return output


def test_example_1() -> None:
    """Run the worked example."""
    assert Solution().countBits(4) == [0, 1, 1, 2, 1]


if __name__ == "__main__":
    test_example_1()
    print("Example test passed.")
