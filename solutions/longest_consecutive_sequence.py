"""Longest Consecutive Sequence.

Return the length of the longest sequence of consecutive integers in an
unsorted list.
"""

from typing import List


class Solution:
    """Start a sequence only at values with no predecessor."""

    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0
        for number in values:
            if number - 1 in values:
                continue
            length = 1
            while number + length in values:
                length += 1
            longest = max(longest, length)
        return longest


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    print("The worked example passed.")
