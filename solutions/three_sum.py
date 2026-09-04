"""3Sum.

Return all unique triplets whose values add to zero.
"""

from typing import List


class Solution:
    """Fix one sorted value and find the other two with pointers."""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        for first in range(len(nums) - 2):
            if first and nums[first] == nums[first - 1]:
                continue
            left, right = first + 1, len(nums) - 1
            while left < right:
                total = nums[first] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[first], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result


if __name__ == "__main__":
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    print("The worked example passed.")
