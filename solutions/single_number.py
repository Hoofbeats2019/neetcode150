"""Single Number.

Given a non-empty array of integers ``nums``, every integer appears twice
except for one. Return the integer that appears only once.

The solution must run in O(n) time and use O(1) extra space.

Examples:
    singleNumber([3, 2, 3]) -> 2
    singleNumber([7, 6, 6, 7, 8]) -> 8

Constraints:
    1 <= len(nums) <= 10_000
    -10_000 <= nums[i] <= 10_000
"""

from typing import List


class Solution:
    """Find the unpaired value by XOR-ing every number once."""

    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for number in nums:
            result ^= number

        return result


def test_worked_examples() -> None:
    solution = Solution()

    assert solution.singleNumber([3, 2, 3]) == 2
    assert solution.singleNumber([7, 6, 6, 7, 8]) == 8


if __name__ == "__main__":
    test_worked_examples()
    print("The worked examples passed.")
