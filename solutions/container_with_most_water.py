"""Container With Most Water.

Find the largest area formed by two vertical lines in an array of heights.
"""

from typing import List


class Solution:
    """Move the pointer at the shorter boundary after each area check."""

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print("The worked example passed.")
