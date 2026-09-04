"""Plus One.

Created: 4 September 2026
Created by: Yanlong Su

You are given an integer array ``digits``, where each ``digits[i]`` is the
``i``th digit of a large integer. The digits are ordered from most significant
to least significant, and the integer has no leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:
    Input: digits = [1, 2, 3, 4]
    Output: [1, 2, 3, 5]
    Explanation: 1234 + 1 = 1235.

Example 2:
    Input: digits = [9, 9, 9]
    Output: [1, 0, 0, 0]

Constraints:
    1 <= len(digits) <= 100
    0 <= digits[i] <= 9

Approach:
    Scan from right to left. Increment the first digit smaller than ``9`` and
    return immediately. Change each trailing ``9`` to ``0`` to propagate the
    carry. If every digit is ``9``, return a new list with a leading ``1``.

Time complexity: O(n)
Space complexity: O(1) auxiliary space
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """Return the digits after incrementing the represented integer by one."""
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] < 9:
                digits[index] += 1
                return digits

            digits[index] = 0

        return [1] + digits


def test_examples() -> None:
    """Run the worked examples after implementing ``plusOne``."""
    solution = Solution()

    assert solution.plusOne([1, 2, 3, 4]) == [1, 2, 3, 5]
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0]


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
