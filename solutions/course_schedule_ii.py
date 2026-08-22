"""Course Schedule II.

Created: 22 August 2026
Created by: Yanlong Su

There are ``numCourses`` courses labeled from 0 to ``numCourses - 1``.
Each pair ``[a, b]`` in ``prerequisites`` means course ``b`` must be taken
before course ``a``.

Return an ordering of courses that allows every course to be completed. If
there are multiple valid orderings, return any of them. If no valid ordering
exists, return an empty list.

Example 1:
    Input: numCourses = 2, prerequisites = [[1, 0]]
    Output: [0, 1]

Example 2:
    Input: numCourses = 4,
           prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    Output: [0, 2, 1, 3]
    Explanation: [0, 1, 2, 3] is also a valid ordering.

Example 3:
    Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
    Output: []

Constraints:
    1 <= numCourses <= 2000
    0 <= len(prerequisites) <= numCourses * (numCourses - 1)
    len(prerequisites[i]) == 2
    0 <= prerequisites[i][0], prerequisites[i][1] < numCourses
    All prerequisite pairs are unique.

Pseudocode:
    findOrder(numCourses, prerequisites):
        build an adjacency list with an edge from each prerequisite to course
        mark every course as unvisited
        create an empty order list

        dfs(course):
            if course is visiting, return false because a cycle was found
            if course is visited, return true because it was already checked
            mark course as visiting
            recursively check every next course
            mark course as visited
            append course to order
            return true

        run DFS from every unvisited course
        return an empty list if any DFS finds a cycle
        reverse order and return it

Time complexity: O(V + E)
Space complexity: O(V + E)
"""

import sys
from typing import List


class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> List[int]:
        """Return a valid ordering of all courses, or an empty list."""
        sys.setrecursionlimit(
            max(sys.getrecursionlimit(), numCourses + 100)
        )

        adjacency_list: list[list[int]] = [
            [] for _ in range(numCourses)
        ]

        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses
        order: list[int] = []

        def dfs(course: int) -> bool:
            if states[course] == visiting:
                return False

            if states[course] == visited:
                return True

            states[course] = visiting

            for next_course in adjacency_list[course]:
                if not dfs(next_course):
                    return False

            states[course] = visited
            order.append(course)
            return True

        for course in range(numCourses):
            if states[course] == unvisited and not dfs(course):
                return []

        order.reverse()
        return order


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().findOrder(2, [[1, 0]]) == [0, 1]


def test_example_2() -> None:
    """Run the second worked example."""
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert Solution().findOrder(4, prerequisites) == [0, 2, 1, 3]


def test_example_3() -> None:
    """Run the cyclic worked example."""
    assert Solution().findOrder(2, [[1, 0], [0, 1]]) == []


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All example tests passed.")
