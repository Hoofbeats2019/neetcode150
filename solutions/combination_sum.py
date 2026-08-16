"""Combination Sum.

Created: 16 August 2026
Created by: Yanlong Su

Given an array of distinct integers ``nums`` and an integer ``target``, return
all unique combinations of values from ``nums`` whose sum is ``target``.

Each value may be selected an unlimited number of times. Two combinations are
the same when they contain each selected value with the same frequency. The
combinations and the values within them may be returned in any order.

Example 1:
    Input: nums = [2, 5, 6, 9], target = 9
    Output: [[2, 2, 5], [9]]

Example 2:
    Input: nums = [3, 4, 5], target = 16
    Output: [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4],
             [3, 4, 4, 5]]

Example 3:
    Input: nums = [3], target = 5
    Output: []

Constraints:
    All elements of ``nums`` are distinct.
    1 <= len(nums) <= 20
    2 <= nums[i] <= 30
    2 <= target <= 30

Pseudocode:
    combinationSum(nums, target):
        create an empty result list
        create an empty current combination

        backtrack(start_index, current_sum):
            if current_sum equals target:
                add a copy of the current combination to result
                return

            if current_sum is greater than target:
                return

            for index from start_index to the end of nums:
                add nums[index] to the current combination
                backtrack(index, current_sum + nums[index])
                remove the last value from the current combination

        backtrack(0, 0)
        return result

Let d = target // min(nums), the maximum recursion depth, and let k be the
number of returned combinations.

Time complexity: O(n^d * d) in the worst case
Space complexity: O(d) auxiliary; O(k * d) for the returned combinations
"""


class Solution:
    def combinationSum(
        self,
        nums: list[int],
        target: int,
    ) -> list[list[int]]:
        """Return unique combinations from nums that sum to target."""
        result: list[list[int]] = []
        current_combination: list[int] = []

        def backtrack(start_index: int, current_sum: int) -> None:
            # VALID RESULT CHECK:
            # The current choices form a result when their sum reaches target.
            is_valid_result = current_sum == target

            if is_valid_result:
                result.append(current_combination.copy())
                return

            # PRUNING:
            # Every candidate is positive, so this sum can never decrease.
            should_prune = current_sum > target

            if should_prune:
                return

            # CHOICES: try each candidate at or after start_index.
            for index in range(start_index, len(nums)):
                chosen_number = nums[index]

                # MAKE THE CHOICE.
                current_combination.append(chosen_number)

                # EXPLORE. Reusing index allows this number to be chosen again.
                backtrack(index, current_sum + chosen_number)

                # UNDO THE CHOICE.
                current_combination.pop()

        backtrack(0, 0)
        return result


def normalize(combinations: list[list[int]]) -> list[tuple[int, ...]]:
    """Normalize combination ordering for the executable examples."""
    return sorted(tuple(sorted(combination)) for combination in combinations)


def test_example_1() -> None:
    actual = Solution().combinationSum([2, 5, 6, 9], 9)
    expected = [[2, 2, 5], [9]]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().combinationSum([3, 4, 5], 16)
    expected = [
        [3, 3, 3, 3, 4],
        [3, 3, 5, 5],
        [4, 4, 4, 4],
        [3, 4, 4, 5],
    ]
    assert normalize(actual) == normalize(expected)


def test_example_3() -> None:
    actual = Solution().combinationSum([3], 5)
    assert actual == []


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
