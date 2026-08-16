"""Subsets.

Created: 16 August 2026
Created by: Yanlong Su

Given an array ``nums`` of unique integers, return all possible subsets of
``nums``.

The solution set must not contain duplicate subsets. The subsets may be
returned in any order.

Example 1:
    Input: nums = [1, 2, 3]
    Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
    Input: nums = [7]
    Output: [[], [7]]

Constraints:
    Every integer in ``nums`` is unique.
    Array-length and integer-value bounds were not supplied.

Time complexity: TBD
Space complexity: TBD
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """Return every distinct subset of nums in any order."""
        # TODO: Implement the user's proposed approach.
        raise NotImplementedError


def normalize(subsets: list[list[int]]) -> list[tuple[int, ...]]:
    """Normalize subset ordering for the executable examples."""
    return sorted(tuple(sorted(subset)) for subset in subsets)


def test_example_1() -> None:
    actual = Solution().subsets([1, 2, 3])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().subsets([7])
    expected = [[], [7]]
    assert normalize(actual) == normalize(expected)


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
