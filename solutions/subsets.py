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

Pseudocode:
    subsets(nums):
        create an empty result list
        create an empty current subset

        backtrack(index):
            valid_result = index equals the length of nums

            if valid_result:
                add a copy of the valid, complete subset to result
                return

            for each choice in [include, exclude]:
                if the choice is include:
                    add nums[index] to the current subset

                backtrack(index + 1)

                if the choice was include:
                    remove nums[index] from the current subset

        backtrack(0)
        return result

Time complexity: O(n * 2^n)
Space complexity: O(n) auxiliary; O(n * 2^n) including the returned subsets
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """Return every distinct subset of nums in any order."""
        result: list[list[int]] = []
        current_subset: list[int] = []

        def backtrack(index: int) -> None:
            """Make an include/exclude choice for ``nums[index]``."""
            # VALID RESULT CHECK:
            # A subset is complete after every number has received an
            # include/exclude decision. Only complete subsets are recorded.
            is_valid_result = index == len(nums)

            if is_valid_result:
                result.append(current_subset.copy())
                return

            # CHOICES: include the current number or exclude it.
            for should_include in (True, False):
                # MAKE THE CHOICE.
                if should_include:
                    current_subset.append(nums[index])

                # EXPLORE after making this choice.
                backtrack(index + 1)

                # UNDO the choice before trying the next one.
                if should_include:
                    current_subset.pop()

        backtrack(0)
        return result


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
