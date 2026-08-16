"""Combination Sum II.

Created: 16 August 2026
Created by: Yanlong Su

Given an array of integers ``candidates``, which may contain duplicates, and
an integer ``target``, return all unique combinations of candidates whose sum
is ``target``.

Each element from ``candidates`` may be chosen at most once within a
combination. The solution set must not contain duplicate combinations. The
combinations and the values within them may be returned in any order.

Example 1:
    Input: candidates = [9, 2, 2, 4, 6, 1, 5], target = 8
    Output: [[1, 2, 5], [2, 2, 4], [2, 6]]

Example 2:
    Input: candidates = [1, 2, 3, 4, 5], target = 7
    Output: [[1, 2, 4], [2, 5], [3, 4]]

Constraints:
    1 <= len(candidates) <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

Pseudocode:
    combinationSum2(candidates, target):
        sort candidates in ascending order
        create an empty result list
        create an empty current state

        backtrack(current_sum, remaining_candidates):
            if current_sum equals target:
                add a copy of the current state to result
                return

            if current_sum is greater than target:
                return

            copy the remaining candidates for this recursion level
            set the previously chosen number to none

            while this level still has candidates:
                pop one candidate

                if it equals the previous choice at this level:
                    skip it

                remember it as the previous choice
                add it to the current state
                recurse with a copy of the candidates still remaining
                remove it from the current state

        backtrack with sum zero and a copy of the sorted candidates
        return result

Time complexity: O(n * 2^n)
Space complexity: O(n^2) auxiliary; O(k * n) for the returned combinations
"""


class Solution:
    def combinationSum2(
        self,
        candidates: list[int],
        target: int,
    ) -> list[list[int]]:
        """Return unique combinations that sum to target."""
        result: list[list[int]] = []
        state: list[int] = []

        # Sorting groups duplicate values together. ``sorted`` also avoids
        # changing the caller's input list.
        sorted_candidates = sorted(candidates)

        def backtrack(
            current_sum: int,
            remaining_candidates: list[int],
        ) -> None:
            # VALID RESULT CHECK:
            # The current choices form a complete result at the target sum.
            if current_sum == target:
                result.append(state.copy())
                return

            # PRUNING:
            # All candidates are positive, so an excessive sum cannot shrink.
            if current_sum > target:
                return

            # Each branch gets its own list. Popping from this local copy
            # therefore cannot consume candidates needed by sibling branches.
            candidates_for_this_level = remaining_candidates.copy()
            previous_chosen_number: int | None = None

            while candidates_for_this_level:
                chosen_number = candidates_for_this_level.pop()

                # Equal values at the same recursion level would create the
                # same combination, so only explore the first one.
                if chosen_number == previous_chosen_number:
                    continue

                previous_chosen_number = chosen_number

                # MAKE THE CHOICE.
                state.append(chosen_number)

                # EXPLORE. Only unchosen candidates are passed forward, which
                # ensures each candidate occurrence is used at most once.
                backtrack(
                    current_sum + chosen_number,
                    candidates_for_this_level.copy(),
                )

                # UNDO THE CHOICE before exploring the next candidate.
                state.pop()

        backtrack(0, sorted_candidates.copy())
        return result


def normalize(combinations: list[list[int]]) -> list[tuple[int, ...]]:
    """Normalize combination ordering for the executable examples."""
    return sorted(tuple(sorted(combination)) for combination in combinations)


def test_example_1() -> None:
    actual = Solution().combinationSum2([9, 2, 2, 4, 6, 1, 5], 8)
    expected = [[1, 2, 5], [2, 2, 4], [2, 6]]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().combinationSum2([1, 2, 3, 4, 5], 7)
    expected = [[1, 2, 4], [2, 5], [3, 4]]
    assert normalize(actual) == normalize(expected)


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
