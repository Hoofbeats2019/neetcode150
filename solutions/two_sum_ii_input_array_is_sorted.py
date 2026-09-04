"""Two Sum II - Input Array Is Sorted.

Return one-based indexes of two distinct sorted-array values whose sum equals
the target.
"""

from typing import List


class Solution:
    """Narrow a pair of pointers according to the current sum."""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            if current < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    print("The worked example passed.")
