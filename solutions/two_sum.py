"""Two Sum.

Return the indexes of two different elements in ``nums`` whose values add to
``target``. Exactly one answer exists.

Examples:
    twoSum([2, 7, 11, 15], 9) -> [0, 1]
    twoSum([3, 2, 4], 6) -> [1, 2]
"""

from typing import List


class Solution:
    """Find each complement among values seen earlier in the list."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes_by_value: dict[int, int] = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in indexes_by_value:
                return [indexes_by_value[complement], index]
            indexes_by_value[number] = index

        return []


def test_worked_examples() -> None:
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]


if __name__ == "__main__":
    test_worked_examples()
    print("The worked examples passed.")
