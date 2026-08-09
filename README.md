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
| [Merge K Sorted Linked Lists](solutions/merge_k_sorted_linked_lists.py) | Linked List | Solved | Merge neighboring lists in balanced rounds | O(n log k) | O(1) |
| [Add Two Numbers](solutions/add_two_numbers.py) | Linked List | Solved | Add corresponding digits while carrying overflow forward | O(max(n, m)) | O(max(n, m)) |
| [Linked List Cycle Detection](solutions/linked_list_cycle_detection.py) | Linked List | Solved | Slow and fast pointers detect whether traversal repeats | O(n) | O(1) |
| [Reorder Linked List](solutions/reorder_linked_list.py) | Linked List | Solved | Split, reverse the second half, then merge alternately | O(n) | O(1) |
| [Remove Nth Node From End of List](solutions/remove_nth_node_from_end_of_list.py) | Linked List | Solved | Keep fast ahead of slow and track slow's previous node | O(n) | O(1) |
| [Copy Linked List with Random Pointer](solutions/copy_linked_list_with_random_pointer.py) | Linked List | Solved | Map each original node to its copied node in two passes | O(n) | O(n) |
| [Find the Duplicate Number](solutions/find_the_duplicate_number.py) | Linked List | Solved | Floyd's cycle detection finds the cycle entrance | O(n) | O(1) |
| [LRU Cache](solutions/lru_cache.py) | Linked List | Solved | Hash map with a doubly linked usage-order list | O(1) average per operation | O(capacity) |

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

### Merge K Sorted Linked Lists

- Merge neighboring lists in rounds so the merged lists remain balanced in size.
- Double the interval between paired list heads after each round.
- An unpaired list remains in place until it can be merged in a later round.
- Relink the existing nodes to avoid allocating a second collection of nodes.
- Each node participates in at most one merge per round, producing O(n log k) time.

### Add Two Numbers

- Traverse both reverse-order lists together from their least significant digits.
- Add the available digits and the carry from the previous position.
- Store `total % 10` in the new result node and carry `total // 10` forward.
- Continue while either list has a node or a final carry remains.

### Linked List Cycle Detection

- Start slow and fast pointers at the head of the list.
- Move the slow pointer one node at a time and the fast pointer two nodes at a time.
- If the pointers meet at the same node, the list contains a cycle.
- If the fast pointer or its next pointer reaches `None`, the list has an end and contains no cycle.

### Reorder Linked List

- Use slow and fast pointers to split the list into two halves.
- Disconnect the halves before reversing the second half to avoid creating a cycle.
- Reverse the second half in place so its nodes are ordered from the original tail inward.
- Merge the halves by alternately attaching one node from each half.
- Relinking the existing nodes preserves their values and uses constant extra space.

### Remove Nth Node From End of List

- Move the fast pointer `n - 1` nodes ahead so slow reaches the node to remove when fast reaches the tail.
- Advance the previous, slow, and fast pointers together while traversing the list.
- Use the previous pointer to bypass the node selected by slow.
- When previous is `None`, slow is the head, so return the second node as the new head.

### Copy Linked List with Random Pointer

- First copy every node and connect the copied list's `next` pointers.
- Map each original node object to its corresponding copied node; values cannot identify nodes because they may repeat.
- Traverse the original list again and use the map to assign each copied node's `random` pointer.
- Looking up the copied random target prevents pointers in the copied list from referring to original nodes.

### Find the Duplicate Number

- Treat each array value as the index of the next position, forming a linked structure.
- Since n + 1 positions point into only n possible positions, the duplicate creates a cycle entrance.
- Move a slow pointer one step and a fast pointer two steps until they meet inside the cycle.
- Reset one pointer to the start and move both one step at a time; their next meeting is the duplicate.
- The pointers use constant extra space and do not modify the input array.

### LRU Cache

- Map every key directly to its doubly linked-list node for average O(1) lookup.
- Keep the least recently used node beside the dummy head and the most recently used node beside the dummy tail.
- A successful `get` and every `put` move the affected node to the most-recently-used end.
- When the cache exceeds its capacity, remove the node beside the head from both the list and the map.
- Dummy boundary nodes avoid special cases when inserting or removing the first or last cache entry.
