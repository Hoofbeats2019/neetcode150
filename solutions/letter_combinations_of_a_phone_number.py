"""Letter Combinations of a Phone Number.

Created: 16 August 2026
Created by: Yanlong Su

Given a string ``digits`` containing digits from 2 through 9 inclusive, return
all possible letter combinations the digits could represent. Each digit maps
to the letters on a telephone keypad, and the combinations may be returned in
any order.

Example 1:
    Input: digits = "34"
    Output: ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]

Example 2:
    Input: digits = ""
    Output: []

Constraints:
    0 <= len(digits) <= 4
    Every character in ``digits`` is between "2" and "9" inclusive.

Pseudocode:
    letter_combinations(digits):
        if digits is empty:
            return []

        create a dictionary mapping each digit to its letters
        create an empty result list
        create an empty current combination

        backtrack(digit_index):
            if digit_index equals the length of digits:
                add the current combination to result
                return

            for each letter mapped to digits[digit_index]:
                add the letter to the current combination
                backtrack(digit_index + 1)
                remove the letter from the current combination

        backtrack(0)
        return result

Time complexity: O(n * 4^n) in the worst case
Space complexity: O(n) auxiliary; O(n * 4^n) including returned strings
"""


class Solution:
    def letter_combinations(self, digits: str) -> list[str]:
        """Return every letter combination represented by digits."""
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result: list[str] = []
        current_combination: list[str] = []

        def backtrack(digit_index: int) -> None:
            # A combination is complete after choosing one letter per digit.
            if digit_index == len(digits):
                result.append("".join(current_combination))
                return

            current_digit = digits[digit_index]

            # Choose one mapped letter for the current digit.
            for letter in digit_to_letters[current_digit]:
                current_combination.append(letter)
                backtrack(digit_index + 1)
                current_combination.pop()

        backtrack(0)
        return result


def test_example_1() -> None:
    actual = Solution().letter_combinations("34")
    expected = ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]
    assert sorted(actual) == sorted(expected)


def test_example_2() -> None:
    actual = Solution().letter_combinations("")
    assert actual == []


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
