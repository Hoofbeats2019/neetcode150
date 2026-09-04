"""Product of Array Except Self.

Return an array where each position is the product of every input value except
the value at that position, without division.
"""

from typing import List


class Solution:
    """Combine products to the left and right of each index."""

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for index, number in enumerate(nums):
            result[index] = prefix
            prefix *= number

        suffix = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= suffix
            suffix *= nums[index]
        return result


if __name__ == "__main__":
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    print("The worked example passed.")
