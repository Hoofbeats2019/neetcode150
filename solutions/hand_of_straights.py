"""Hand of Straights.

Created: 2 September 2026
Created by: Yanlong Su

You are given an integer array ``hand`` where ``hand[i]`` is the value written
on the ith card and an integer ``groupSize``.

Rearrange the cards into groups of ``groupSize`` cards such that each group's
card values increase consecutively by 1. Return ``True`` when this is
possible; otherwise, return ``False``.

Example 1:
    Input: hand = [1, 2, 4, 2, 3, 5, 3, 4], groupSize = 4
    Output: True

    The groups can be [1, 2, 3, 4] and [2, 3, 4, 5].

Example 2:
    Input: hand = [1, 2, 3, 3, 4, 5, 6, 7], groupSize = 4
    Output: False

Constraints:
    1 <= len(hand) <= 10,000
    0 <= hand[i] <= 1,000
    1 <= groupSize <= len(hand)

Approach:
    Count each card value, then sort the hand. For every card that has not
    already been used, use it to start a group and consume one copy of each
    required consecutive value. If a required value has no remaining copy,
    the arrangement is impossible.

Time complexity: O(n log n)
Space complexity: O(n)
"""

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """Return whether the cards can be arranged into valid groups."""
        if len(hand) % groupSize != 0:
            return False

        frequency = Counter(hand)
        hand.sort()

        for card in hand:
            if frequency[card] == 0:
                continue

            for offset in range(groupSize):
                required_card = card + offset

                if frequency[required_card] == 0:
                    return False

                frequency[required_card] -= 1

        return True


def test_example_1() -> None:
    """Run the first worked example."""
    expected = True
    actual = Solution().isNStraightHand([1, 2, 4, 2, 3, 5, 3, 4], 4)
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = False
    actual = Solution().isNStraightHand([1, 2, 3, 3, 4, 5, 6, 7], 4)
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
