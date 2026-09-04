"""Contains Duplicate.

Given an integer list, return ``True`` when any value appears at least twice
and ``False`` when every value is distinct.

Examples:
    containsDuplicate([1, 2, 3, 1]) -> True
    containsDuplicate([1, 2, 3, 4]) -> False

Constraints:
    1 <= len(nums) <= 100_000
    -1_000_000_000 <= nums[i] <= 1_000_000_000
"""

from typing import List


class Solution:
    """Detect a repeated value with a set of values seen so far."""

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()

        for number in nums:
            if number in seen:
                return True
            seen.add(number)

        return False


def test_worked_examples() -> None:
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 1]) is True
    assert solution.containsDuplicate([1, 2, 3, 4]) is False


if __name__ == "__main__":
    test_worked_examples()
    print("The worked examples passed.")
