"""Partition Labels.

Created: 2 September 2026
Created by: Yanlong Su

You are given a string ``s`` consisting of lowercase English letters. Split
``s`` into as many substrings as possible while ensuring each letter appears
in at most one substring. Return the lengths of those substrings in their
original order.

Example 1:
    Input: s = "xyxxyzbzbbisl"
    Output: [5, 5, 1, 1, 1]
    Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

Example 2:
    Input: s = "abcabc"
    Output: [6]

Constraints:
    1 <= len(s) <= 100
    s contains lowercase English letters only.

Approach:
    Record the last index of each character. Scan the string while tracking
    the furthest last index of any character in the current partition. When
    the scan reaches that boundary, all characters in the partition are
    contained within it, so record its length and begin the next partition.

Time complexity: O(n)
Space complexity: O(1), because the input contains only lowercase English
letters.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """Return the lengths of the maximum valid partition of ``s``."""
        last_index = {character: index for index, character in enumerate(s)}
        partition_lengths = []
        start = 0
        end = 0

        for index, character in enumerate(s):
            end = max(end, last_index[character])

            if index == end:
                partition_lengths.append(end - start + 1)
                start = index + 1

        return partition_lengths


def test_example_1() -> None:
    """Run the first worked example."""
    expected = [5, 5, 1, 1, 1]
    actual = Solution().partitionLabels("xyxxyzbzbbisl")
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    """Run the second worked example."""
    expected = [6]
    actual = Solution().partitionLabels("abcabc")
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
