"""Find Median From Data Stream.

Created: 16 August 2026
Created by: Yanlong Su

The median is the middle value in an ordered integer list. When the list has
an even number of values, the median is the mean of its two middle values.

Implement ``MedianFinder`` so integers can be added from a data stream and the
median of all values received so far can be returned.

Example 1:
    Input:
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(2)
        median_finder.findMedian()
        median_finder.addNum(3)
        median_finder.findMedian()
    Output: 1.5, 2.0

Constraints:
    -10^5 <= num <= 10^5
    At least one value is added before ``findMedian`` is called.
    At most 5 * 10^4 calls are made to ``addNum`` and ``findMedian``.

Pseudocode:
    constructor:
        small = empty max-heap
        large = empty min-heap

    addNum(num):
        if small is empty or num <= maximum of small:
            push num into small
        otherwise:
            push num into large

        if size(small) > size(large) + 1:
            move the maximum of small into large
        else if size(large) > size(small):
            move the minimum of large into small

    findMedian():
        if size(small) > size(large):
            return maximum of small
        return (maximum of small + minimum of large) / 2
"""

from heapq import heappop, heappush


class MedianFinder:
    def __init__(self) -> None:
        """Initialize heaps for the smaller and larger halves."""
        # Negated values make Python's min-heap act like a max-heap.
        self.small: list[int] = []
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        """Add num while keeping the two heaps ordered and balanced."""
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
        elif len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        """Return the median of all numbers added so far."""
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2


def test_example_1() -> None:
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5

    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0


if __name__ == "__main__":
    test_example_1()
    print("Example test passed.")
