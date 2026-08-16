"""Permutations.

Created: 16 August 2026
Created by: Yanlong Su

Given an array ``nums`` of unique integers, return all possible permutations.
The permutations may be returned in any order.

Example 1:
    Input: nums = [1, 2, 3]
    Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3],
             [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Example 2:
    Input: nums = [7]
    Output: [[7]]

Constraints:
    Every integer in ``nums`` is unique.
    Array-length and integer-value bounds were not supplied.

Pseudocode:
    permute(nums):
        create an empty result list
        create an empty current state

        backtrack(current_state, remaining_nums):
            if the length of current_state equals the length of nums:
                add a copy of current_state to result
                return

            for each number in remaining_nums:
                copy remaining_nums into new_remaining_nums
                remove the chosen number from new_remaining_nums
                add the chosen number to current_state
                backtrack(current_state, new_remaining_nums)
                remove the chosen number from current_state

        backtrack(current_state, nums)
        return result

Time complexity: O(n * n!)
Space complexity: O(n^2) auxiliary; O(n * n!) for returned permutations
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """Return every permutation of nums in any order."""
        result: list[list[int]] = []
        current_state: list[int] = []

        def backtrack(remaining_nums: list[int]) -> None:
            # VALID RESULT CHECK:
            # A permutation is complete after every input number is chosen.
            is_valid_result = len(current_state) == len(nums)

            if is_valid_result:
                result.append(current_state.copy())
                return

            # CHOICES: each remaining number can occupy the next position.
            for chosen_number in remaining_nums:
                # Give this branch its own remaining-numbers list.
                new_remaining_nums = remaining_nums.copy()
                new_remaining_nums.remove(chosen_number)

                # MAKE THE CHOICE.
                current_state.append(chosen_number)

                # EXPLORE with only the numbers that are still unused.
                backtrack(new_remaining_nums)

                # UNDO THE CHOICE before exploring the next branch.
                current_state.pop()

        backtrack(nums.copy())
        return result


def normalize(permutations: list[list[int]]) -> list[tuple[int, ...]]:
    """Normalize permutation ordering for the executable examples."""
    return sorted(tuple(permutation) for permutation in permutations)


def test_example_1() -> None:
    actual = Solution().permute([1, 2, 3])
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().permute([7])
    assert actual == [[7]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
