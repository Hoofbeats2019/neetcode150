"""Kth Largest Element in a Stream.

Created: 15 August 2026
Created by: Yanlong Su

Design a class that finds the kth largest integer in a stream of values,
including duplicates. The stream is not necessarily sorted. For example, the
second largest integer in ``[1, 2, 3, 3]`` is ``3``.

* ``KthLargest(k, nums)`` initializes the stream with ``nums``.
* ``add(val)`` adds ``val`` to the stream and returns its kth largest value.

Example:
    Input:
        ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5],
         "add", [6], "add", [7], "add", [8]]
    Output:
        [null, 3, 3, 3, 5, 6]

Executable example:
    >>> kth_largest = KthLargest(3, [1, 2, 3, 3])
    >>> kth_largest.add(3)
    3
    >>> kth_largest.add(5)
    3
    >>> kth_largest.add(6)
    3
    >>> kth_largest.add(7)
    5
    >>> kth_largest.add(8)
    6

Constraints:
    1 <= k <= 10^4
    0 <= nums.length <= 10^4
    -10^4 <= nums[i], val <= 10^4
    At most 10^4 calls are made to ``add``.

Pseudocode:
    KthLargest(k, nums):
        store k
        sort nums in descending order
        store the sorted nums

    add(val):
        append val to nums
        sort nums in descending order
        return nums[k - 1]
"""


class KthLargest:
    """Track the kth largest value in a stream."""

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]


def test_example_1() -> None:
    kth_largest = KthLargest(3, [1, 2, 3, 3])
    assert kth_largest.add(3) == 3
    assert kth_largest.add(5) == 3
    assert kth_largest.add(6) == 3
    assert kth_largest.add(7) == 5
    assert kth_largest.add(8) == 6


if __name__ == "__main__":
    test_example_1()
    print("Example test passed.")
