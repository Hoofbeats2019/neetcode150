"""Decode Ways.

Created: 26 August 2026
Created by: Yanlong Su

A string of uppercase English letters can be encoded using the mapping
``A -> 1``, ``B -> 2``, through ``Z -> 26``. To decode a digit string, group
its digits and map each group back to a letter. A group cannot have a leading
zero, so, for example, ``01`` is invalid.

Given a string ``s`` containing only digits, return the number of ways it can
be decoded. The answer fits in a 32-bit integer.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation: The valid decodings are ``1 2`` (AB) and ``12`` (L).

Example 2:
    Input: s = "01"
    Output: 0
    Explanation: ``01`` cannot be mapped because it has a leading zero.

Constraints:
    1 <= len(s) <= 100
    s contains only digits

Pseudocode:
    numDecodings(s):
        create an empty memo

        decode(prefix_length):
            if prefix_length is 0, return 1
            if prefix_length is already in memo, return its stored result

            ways = 0

            if the last digit is between 1 and 9:
                add decode(prefix_length - 1) to ways

            if the last two digits are between 10 and 26:
                add decode(prefix_length - 2) to ways

            store ways in memo for prefix_length
            return the stored result

        return decode(length of s)

Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """Return the number of valid ways to decode ``s``."""
        memo: dict[int, int] = {}

        def decode(prefix_length: int) -> int:
            if prefix_length == 0:
                return 1

            if prefix_length in memo:
                return memo[prefix_length]

            ways = 0

            if s[prefix_length - 1] != "0":
                ways += decode(prefix_length - 1)

            if prefix_length >= 2:
                last_two_digits = int(s[prefix_length - 2 : prefix_length])

                if 10 <= last_two_digits <= 26:
                    ways += decode(prefix_length - 2)

            memo[prefix_length] = ways

            return memo[prefix_length]

        return decode(len(s))


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().numDecodings("12") == 2


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().numDecodings("01") == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
