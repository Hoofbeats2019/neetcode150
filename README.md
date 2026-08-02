# NeetCode 150

My solutions and learning notes for the NeetCode 150 roadmap.

## Progress

| Problem | Category | Status | Approach | Time | Space |
| --- | --- | --- | --- | --- | --- |
| [Largest Rectangle in Histogram](solutions/largest_rectangle_in_histogram.py) | Stack | Solved | Monotonic stack with left and right boundaries | O(n) | O(n) |
| [Binary Search](solutions/binary_search.py) | Binary Search | Solved | Recursive binary search with index boundaries | O(log n) | O(log n) |

## Learning notes

### Largest Rectangle in Histogram

- Each bar can extend until it reaches a strictly shorter bar on either side.
- A monotonic stack finds those boundaries efficiently.
- Each index is pushed and popped at most once, producing linear runtime.

### Binary Search

- Compare the target with the middle element of the current search range.
- Search the left half when the target is smaller and the right half when it is larger.
- Passing index boundaries avoids copying list slices and preserves logarithmic runtime.
- The search ends unsuccessfully when the left boundary moves beyond the right boundary.
