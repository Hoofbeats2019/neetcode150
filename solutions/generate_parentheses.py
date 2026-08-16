"""Generate Parentheses.

Created: 16 August 2026
Created by: Yanlong Su

Given an integer ``n``, return all well-formed parentheses strings that can be
generated with ``n`` pairs of parentheses. The strings may be returned in any
order.

Example 1:
    Input: n = 1
    Output: ["()"]

Example 2:
    Input: n = 3
    Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Constraints:
    1 <= n <= 7

Pseudocode:
    generate_parenthesis(n):
        create an empty result list
        create an explored set containing the empty string

        backtrack(current_state):
            if the length of current_state equals 2 * n:
                add current_state to result
                return

            for every insertion position in current_state:
                insert "()" at that position to create a new state

                if the new state has already been explored:
                    continue

                add the new state to explored
                backtrack(new_state)

        backtrack("")
        return result

Time complexity: O(n^2 * C_n), where C_n is the nth Catalan number
Space complexity: O(n * C_n), including explored states and returned strings
"""


class Solution:
    def generate_parenthesis(self, n: int) -> list[str]:
        """Return every well-formed string containing ``n`` pairs."""
        result: list[str] = []
        explored: set[str] = {""}

        def backtrack(current_state: str) -> None:
            # VALID RESULT CHECK:
            # Inserting a complete pair preserves well-formedness, so a state
            # with n pairs is a valid result.
            is_valid_result = len(current_state) == 2 * n

            if is_valid_result:
                result.append(current_state)
                return

            # CHOICES: insert a complete pair at every possible position.
            for insertion_position in range(len(current_state) + 1):
                new_state = (
                    current_state[:insertion_position]
                    + "()"
                    + current_state[insertion_position:]
                )

                # PRUNE duplicate states created by different insertions.
                if new_state in explored:
                    continue

                explored.add(new_state)
                backtrack(new_state)

        backtrack("")
        return result


def normalize(parentheses: list[str]) -> list[str]:
    """Normalize result ordering for the executable examples."""
    return sorted(parentheses)


def test_example_1() -> None:
    actual = Solution().generate_parenthesis(1)
    expected = ["()"]
    assert normalize(actual) == normalize(expected)


def test_example_2() -> None:
    actual = Solution().generate_parenthesis(3)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert normalize(actual) == normalize(expected)


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
