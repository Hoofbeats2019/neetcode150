"""Task Scheduler.

Created: 16 August 2026
Created by: Yanlong Su

You are given an array of CPU tasks, where each task is an uppercase English
letter from ``A`` to ``Z``, and an integer ``n``.

Each CPU cycle can complete one task, and tasks may be completed in any order.
Identical tasks must be separated by at least ``n`` CPU cycles. Return the
minimum number of CPU cycles required to complete all tasks.

Example 1:
    Input: tasks = ["X", "X", "Y", "Y"], n = 2
    Output: 5

    One possible sequence is X -> Y -> idle -> X -> Y.

Example 2:
    Input: tasks = ["A", "A", "A", "B", "C"], n = 3
    Output: 9

    One possible sequence is
    A -> B -> C -> idle -> A -> idle -> idle -> idle -> A.

Constraints:
    1 <= tasks.length <= 10^4
    0 <= n <= 100

Pseudocode:
    leastInterval(tasks, n):
        count how many copies remain for each task
        place all available tasks in a max heap ordered by remaining count
        create a cooldown queue
        start time at zero

        while the heap or cooldown queue is not empty:
            increment time by one
            move tasks whose ready time has arrived back into the heap

            if the heap is not empty:
                run the task with the largest remaining count
                decrease its remaining count

                if copies remain:
                    record when it can next run and add it to the cooldown queue

        return time
"""

from collections import Counter, deque
from heapq import heapify, heappop, heappush
from typing import Deque, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Return the minimum cycles needed to finish every task."""
        # Count how many copies of each task still need to run.
        task_counts = Counter(tasks)

        # Python has a min-heap, so negative counts make the largest count
        # appear at the top of the heap.
        available = [-count for count in task_counts.values()]
        heapify(available)

        # Each queue entry is (negative remaining count, next ready time).
        cooldown: Deque[tuple[int, int]] = deque()
        time = 0

        # Continue until every available and cooling-down task is completed.
        while available or cooldown:
            time += 1

            # Return every task whose cooldown has finished to the heap.
            while cooldown and cooldown[0][1] <= time:
                remaining_count, _ = cooldown.popleft()
                heappush(available, remaining_count)

            if available:
                # Run the available task with the most copies remaining.
                # Adding one moves its negative count one step toward zero.
                remaining_count = heappop(available) + 1

                if remaining_count < 0:
                    # There must be n complete cycles between identical tasks.
                    ready_time = time + n + 1
                    cooldown.append((remaining_count, ready_time))

        return time


def test_example_1() -> None:
    solution = Solution()
    actual = solution.leastInterval(["X", "X", "Y", "Y"], 2)
    expected = 5
    assert actual == expected, f"Expected {expected}, but received {actual}"


def test_example_2() -> None:
    solution = Solution()
    actual = solution.leastInterval(["A", "A", "A", "B", "C"], 3)
    expected = 9
    assert actual == expected, f"Expected {expected}, but received {actual}"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
