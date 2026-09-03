"""Minimum Interval to Include Each Query.

Created: 3 September 2026
Created by: Yanlong Su

Given inclusive integer intervals and query points, return the length of the
shortest interval containing each query. Return ``-1`` when no interval
contains a query.

Example 1:
    Input: intervals = [[1, 3], [2, 3], [3, 7], [6, 6]]
           queries = [2, 3, 1, 7, 6, 8]
    Output: [2, 2, 3, 5, 1, -1]

Constraints:
    1 <= len(intervals), len(queries) <= 100,000
    1 <= left_i <= right_i <= 10,000,000
    1 <= queries[j] <= 10,000,000

Approach:
    Sort intervals and indexed queries by their values. For each query, add
    every interval that has started to a min-heap ordered by interval length.
    Remove heap entries that end before the query. The remaining top entry, if
    any, is the shortest interval that contains the query.

Time complexity: O((n + q) log(n + q))
Space complexity: O(n + q)
"""

import heapq
from typing import List, Tuple


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """Return the shortest containing interval length for each query."""
        intervals.sort(key=lambda interval: interval[0])
        indexed_queries = sorted(
            (query, index) for index, query in enumerate(queries)
        )
        output = [-1] * len(queries)
        active_intervals: List[Tuple[int, int]] = []
        interval_index = 0

        for query, query_index in indexed_queries:
            while (
                interval_index < len(intervals)
                and intervals[interval_index][0] <= query
            ):
                left, right = intervals[interval_index]
                heapq.heappush(active_intervals, (right - left + 1, right))
                interval_index += 1

            while active_intervals and active_intervals[0][1] < query:
                heapq.heappop(active_intervals)

            if active_intervals:
                output[query_index] = active_intervals[0][0]

        return output


def test_example_1() -> None:
    """Run the worked example."""
    expected = [2, 2, 3, 5, 1, -1]
    actual = Solution().minInterval(
        [[1, 3], [2, 3], [3, 7], [6, 6]], [2, 3, 1, 7, 6, 8]
    )
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    print("The example test passed.")
