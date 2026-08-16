"""Subsets II.

Created: 16 August 2026
Created by: Yanlong Su

Given an array ``nums`` of integers, which may contain duplicates, return all
possible subsets.

The solution must not contain duplicate subsets. The subsets may be returned
in any order.

Example 1:
    Input: nums = [1, 2, 1]
    Output: [[], [1], [1, 2], [1, 1], [1, 2, 1], [2]]

Example 2:
    Input: nums = [7, 7]
    Output: [[], [7], [7, 7]]

Constraints:
    1 <= len(nums) <= 11
    -20 <= nums[i] <= 20

Pseudocode:
    subsetsWithDup(nums):
        create a sorted copy of nums
        create an empty result list
        create an empty current subset

        backtrack(start_index):
            add a copy of the current subset to result
            create an empty processed-at-this-level dictionary

            for each index from start_index to the end of the sorted numbers:
                choose the number at index

                if the number is already processed at this level:
                    skip it

                mark the number as processed at this level
                add the number to the current subset
                backtrack(index + 1)
                remove the number from the current subset

        backtrack(0)
        return result

Time complexity: O(n * 2^n)
Space complexity: O(n) auxiliary; O(n * 2^n) including the returned subsets
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """Return every distinct subset of nums in any order."""
        result: list[list[int]] = []
        current_subset: list[int] = []

        # Sorting gives every subset a consistent value order. ``sorted``
        # avoids changing the caller's input list.
        sorted_nums = sorted(nums)

        def backtrack(start_index: int) -> None:
            # Every partial subset is a valid result.
            result.append(current_subset.copy())

            # This dictionary belongs only to the current recursion level.
            processed_at_this_level: dict[int, str] = {}

            for index in range(start_index, len(sorted_nums)):
                chosen_number = sorted_nums[index]

                # PRUNING: an equal sibling choice would reproduce every
                # subset already explored from this value at this level.
                if processed_at_this_level.get(chosen_number) == "processed":
                    continue

                processed_at_this_level[chosen_number] = "processed"

                # MAKE THE CHOICE.
                current_subset.append(chosen_number)

                # EXPLORE using only the numbers after this occurrence.
                backtrack(index + 1)

                # UNDO THE CHOICE before exploring the next candidate.
                current_subset.pop()

        backtrack(0)
        return result


def normalize(subsets: list[list[int]]) -> list[tuple[int, ...]]:
    """Normalize subset ordering for the executable examples."""
    return sorted(tuple(sorted(subset)) for subset in subsets)


def test_example_1() -> None:
    actual = Solution().subsetsWithDup([1, 2, 1])
    expected = [[], [1], [1, 2], [1, 1], [1, 2, 1], [2]]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().subsetsWithDup([7, 7])
    expected = [[], [7], [7, 7]]
    assert normalize(actual) == normalize(expected)


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
