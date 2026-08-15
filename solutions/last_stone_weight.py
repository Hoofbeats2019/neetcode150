"""Last Stone Weight.

Created: 15 August 2026
Created by: Yanlong Su

You are given an array of integers ``stones`` where ``stones[i]`` represents
the weight of the ith stone.

At each step, choose the two heaviest stones with weights ``x`` and ``y`` and
smash them together:

* If ``x == y``, both stones are destroyed.
* If ``x < y``, the stone of weight ``x`` is destroyed and the other stone has
  the new weight ``y - x``.

Continue until no more than one stone remains. Return the weight of the last
remaining stone, or return 0 if no stones remain.

Example 1:
    Input: stones = [2, 3, 6, 2, 4]
    Output: 1

    Smash 6 and 4 to leave 2: [2, 3, 2, 2].
    Smash 3 and 2 to leave 1: [1, 2, 2].
    Smash 2 and 2: [1].

Example 2:
    Input: stones = [1, 2]
    Output: 1

Executable examples:
    >>> solution = Solution()
    >>> solution.lastStoneWeight([2, 3, 6, 2, 4])
    1
    >>> solution.lastStoneWeight([1, 2])
    1

Constraints:
    1 <= stones.length <= 20
    1 <= stones[i] <= 100

Pseudocode:
    lastStoneWeight(stones):
        sort stones in increasing order

        while the length of stones is greater than 1:
            first = remove the last item
            second = remove the last item
            remaining = first - second

            if remaining is greater than 0:
                insert remaining into its correct sorted position

        if stones is empty:
            return 0

        return the only remaining stone
"""

from bisect import insort
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Return the final stone's weight after repeatedly smashing stones."""
        stones.sort()

        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            remaining = first - second

            if remaining > 0:
                insort(stones, remaining)

        if not stones:
            return 0

        return stones[0]


def test_example_1() -> None:
    solution = Solution()
    actual = solution.lastStoneWeight([2, 3, 6, 2, 4])
    expected = 1
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.lastStoneWeight([1, 2])
    expected = 1
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
