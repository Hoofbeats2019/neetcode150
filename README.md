# NeetCode 150

My solutions and learning notes for the NeetCode 150 roadmap.

## Repository standards

The following rules apply to every problem and solution in this repository:

- Include the problem description in the solution file.
- Include worked examples with their inputs and expected outputs.
- Provide test functions in the solution file so the worked examples can be
  tested directly by running that file.
- Include unit tests in the `tests` directory, covering the worked examples and
  relevant edge cases.

## Progress

| Problem | Category | Status | Approach | Time | Space |
| --- | --- | --- | --- | --- | --- |
| [Largest Rectangle in Histogram](solutions/largest_rectangle_in_histogram.py) | Stack | Solved | Monotonic stack with left and right boundaries | O(n) | O(n) |
| [Binary Search](solutions/binary_search.py) | Binary Search | Solved | Recursive binary search with index boundaries | O(log n) | O(log n) |
| [Search a 2D Matrix](solutions/search_a_2d_matrix.py) | Binary Search | Solved | Binary search for the row, then within the row | O(log(m x n)) | O(1) |
| [Koko Eating Bananas](solutions/koko_eating_bananas.py) | Binary Search | Solved | Binary search for the minimum feasible eating rate | O(n log m) | O(1) |
| [Find Minimum in Rotated Sorted Array](solutions/find_minimum_in_rotated_sorted_array.py) | Binary Search | Solved | Compare the middle and rightmost elements to locate the rotation point | O(log n) | O(1) |
| [Search in Rotated Sorted Array](solutions/search_in_rotated_sorted_array.py) | Binary Search | Solved | Find the rotation point, choose the target's sorted side, then binary search | O(log n) | O(1) |
| [Median of Two Sorted Arrays](solutions/median_of_two_sorted_arrays.py) | Binary Search | Solved | Binary search for a valid partition across both arrays | O(log(min(m, n))) | O(1) |
| [Reverse Linked List](solutions/reverse_linked_list.py) | Linked List | Solved | Iteratively redirect each node to its previous node | O(n) | O(1) |
| [Merge Two Sorted Linked Lists](solutions/merge_two_sorted_linked_lists.py) | Linked List | Solved | Compare current nodes and append the smaller node | O(n + m) | O(1) |

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

### Search a 2D Matrix

- Binary search first identifies the only row whose range can contain the target.
- A second binary search looks for the target within that row.
- Index boundaries avoid copying matrix elements or creating another list.
- The two searches take O(log m + log n), equivalent to O(log(m x n)).

### Koko Eating Bananas

- The possible eating rates range from 1 to the largest pile.
- At rate `k`, a pile requires `ceil(pile / k)` hours; integer ceiling division computes this as `(pile + k - 1) // k`.
- If a rate is fast enough, every higher rate is also fast enough, so feasibility is monotonic.
- Binary search keeps a feasible middle rate as a candidate and discards a middle rate that is too slow.

### Find Minimum in Rotated Sorted Array

- Comparing the middle element with the rightmost element identifies which half contains the rotation point.
- When the middle element is greater, the minimum must be strictly to its right.
- Otherwise, the middle element might be the minimum, so it remains in the search range.
- The boundaries eventually meet at the minimum element.

### Search in Rotated Sorted Array

- First, binary search for the index of the minimum element, which is the rotation point.
- The rotation point divides the array into two ascending sections.
- Compare the target with the first element to choose the left or right sorted section.
- Run a standard binary search only within the selected section.
- The two consecutive binary searches take O(log n) time in total and O(1) space.

### Median of Two Sorted Arrays

- Always binary search the shorter array so every partition considered in the longer array remains valid.
- Choose the second partition so the combined left side contains half of all elements.
- A partition is valid when both left-side boundary values are no greater than the opposite right-side boundary values.
- For an odd total length, the median is the largest left-side value; for an even total length, average the largest left-side and smallest right-side values.

### Reverse Linked List

- Keep references to the previous, current, and next nodes while traversing the list.
- Save the next node before changing the current node's `next` pointer, or the rest of the list will be lost.
- Redirect the current node to the previous node, then advance both traversal references.
- When traversal finishes, the previous node is the new head of the reversed list.

### Merge Two Sorted Linked Lists

- Keep references to both the head and tail of the merged result.
- Compare the current nodes and attach the node with the smaller value.
- Advance only the input list whose node was attached.
- When one list is exhausted, attach the remaining part of the other sorted list.
