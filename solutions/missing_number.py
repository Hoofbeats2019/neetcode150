"""Missing Number.

Created: 5 September 2026
Created by: Yanlong Su

Given an array ``nums`` containing ``n`` distinct integers in the range
``[0, n]``, return the single number in that range that is missing from
``nums``.

Example 1:
    Input: nums = [1, 2, 3]
    Output: 0
    Explanation: The range is [0, 3], and 0 does not appear in nums.

Example 2:
    Input: nums = [0, 2]
    Output: 1

Constraints:
    1 <= len(nums) <= 1000

Approach:
    XOR every number from 0 through ``n``, then XOR every value in ``nums``.
    Each present value appears twice and cancels itself out, leaving only the
    missing value.

Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """Return the number missing from the range 0 through ``len(nums)``."""
        result = 0

        for number in range(len(nums) + 1):
            result ^= number

        for number in nums:
            result ^= number

        return result


def test_examples() -> None:
    """Run the worked examples."""
    solution = Solution()

    assert solution.missingNumber([1, 2, 3]) == 0
    assert solution.missingNumber([0, 2]) == 1


if __name__ == "__main__":
    test_examples()
    print("Example tests passed.")
