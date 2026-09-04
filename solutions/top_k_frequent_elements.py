"""Top K Frequent Elements.

Return the ``k`` values that occur most often in an integer list.

Example: topKFrequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2].
"""

from collections import Counter
from typing import List


class Solution:
    """Bucket values by frequency, then read buckets from high to low."""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for number, count in frequency.items():
            buckets[count].append(number)

        result: list[int] = []
        for count in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[count])
            if len(result) >= k:
                return result[:k]
        return result


if __name__ == "__main__":
    assert set(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    print("The worked example passed.")
