"""Multiply Strings.

Created: 4 September 2026
Created by: Yanlong Su

You are given two strings ``num1`` and ``num2`` that represent non-negative
integers. Return their product as a string.

Neither input contains a leading zero unless it is ``"0"`` itself. Do not use
a built-in conversion to turn either input directly into an integer.

Example 1:
    Input: num1 = "3", num2 = "4"
    Output: "12"

Example 2:
    Input: num1 = "111", num2 = "222"
    Output: "24642"

Constraints:
    1 <= len(num1), len(num2) <= 200
    num1 and num2 consist of digits only.

Approach:
    Iterate over both strings from right to left. For every pair of digits,
    add its product to the matching positions in a result array. Store the
    ones digit at the right position and carry the remaining value left.

Time complexity: O(m * n)
Space complexity: O(m + n)
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Return the product of two non-negative integer strings."""
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for first_index in range(len(num1) - 1, -1, -1):
            first_digit = ord(num1[first_index]) - ord("0")

            for second_index in range(len(num2) - 1, -1, -1):
                second_digit = ord(num2[second_index]) - ord("0")
                right_position = first_index + second_index + 1
                left_position = first_index + second_index
                total = result[right_position] + first_digit * second_digit

                result[right_position] = total % 10
                result[left_position] += total // 10

        first_nonzero = 0
        while first_nonzero < len(result) - 1 and result[first_nonzero] == 0:
            first_nonzero += 1

        return "".join(str(digit) for digit in result[first_nonzero:])


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.multiply("3", "4") == "12"
    assert solution.multiply("111", "222") == "24642"


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
