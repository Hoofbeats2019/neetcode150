"""Merge Triplets to Form Target.

Created: 2 September 2026
Created by: Yanlong Su

You are given a list of integer triplets and a target triplet. In one
operation, choose two different triplets and replace one with the
coordinate-wise maximum of both triplets. Return ``True`` if the target can
be obtained as a triplet, otherwise return ``False``.

Example 1:
    Input: triplets = [[1, 2, 3], [7, 1, 1]], target = [7, 2, 3]
    Output: True

Example 2:
    Input: triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 5]], target = [5, 4, 6]
    Output: False

Constraints:
    1 <= len(triplets) <= 1,000
    1 <= triplets[i][j], target[j] <= 100

Approach:
    Ignore any triplet that exceeds the target in at least one coordinate,
    because coordinate-wise maxima cannot decrease it later. Among the safe
    triplets, record whether each target coordinate appears exactly. The
    target is reachable precisely when all three coordinates are available to
    merge.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """Return whether coordinate-wise merges can produce ``target``."""
        has_x = False
        has_y = False
        has_z = False

        for triplet in triplets:
            if any(value > target[index] for index, value in enumerate(triplet)):
                continue

            has_x = has_x or triplet[0] == target[0]
            has_y = has_y or triplet[1] == target[1]
            has_z = has_z or triplet[2] == target[2]

            if has_x and has_y and has_z:
                return True

        return False


def test_example_1() -> None:
    """Run the first worked example."""
    expected = True
    actual = Solution().mergeTriplets([[1, 2, 3], [7, 1, 1]], [7, 2, 3])
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = False
    actual = Solution().mergeTriplets([[2, 5, 6], [1, 4, 4], [5, 7, 5]], [5, 4, 6])
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
