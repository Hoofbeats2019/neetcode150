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
| [Reverse Nodes in K-Group](solutions/reverse_nodes_in_k_group.py) | Linked List | Solved | Scan ahead, then iteratively reverse each complete group | O(n) | O(1) |
| [Merge Two Sorted Linked Lists](solutions/merge_two_sorted_linked_lists.py) | Linked List | Solved | Compare current nodes and append the smaller node | O(n + m) | O(1) |
| [Merge K Sorted Linked Lists](solutions/merge_k_sorted_linked_lists.py) | Linked List | Solved | Merge neighboring lists in balanced rounds | O(n log k) | O(1) |
| [Add Two Numbers](solutions/add_two_numbers.py) | Linked List | Solved | Add corresponding digits while carrying overflow forward | O(max(n, m)) | O(max(n, m)) |
| [Linked List Cycle Detection](solutions/linked_list_cycle_detection.py) | Linked List | Solved | Slow and fast pointers detect whether traversal repeats | O(n) | O(1) |
| [Reorder Linked List](solutions/reorder_linked_list.py) | Linked List | Solved | Split, reverse the second half, then merge alternately | O(n) | O(1) |
| [Remove Nth Node From End of List](solutions/remove_nth_node_from_end_of_list.py) | Linked List | Solved | Keep fast ahead of slow and track slow's previous node | O(n) | O(1) |
| [Copy Linked List with Random Pointer](solutions/copy_linked_list_with_random_pointer.py) | Linked List | Solved | Map each original node to its copied node in two passes | O(n) | O(n) |
| [Find the Duplicate Number](solutions/find_the_duplicate_number.py) | Linked List | Solved | Floyd's cycle detection finds the cycle entrance | O(n) | O(1) |
| [LRU Cache](solutions/lru_cache.py) | Linked List | Solved | Hash map with a doubly linked usage-order list | O(1) average per operation | O(capacity) |
| [Invert Binary Tree](solutions/invert_binary_tree.py) | Trees | Solved | Recursively swap each node's left and right subtrees | O(n) | O(h) |
| [Maximum Depth of Binary Tree](solutions/maximum_depth_of_binary_tree.py) | Trees | Solved | Recursively compare the left and right subtree depths | O(n) | O(h) |
| [Diameter of Binary Tree](solutions/diameter_of_binary_tree.py) | Trees | Solved | Recursively combine left and right subtree depths | O(n) | O(h) |
| [Balanced Binary Tree](solutions/balanced_binary_tree.py) | Trees | Solved | Return each subtree's balance state and height from DFS | O(n) | O(h) |
| [Same Binary Tree](solutions/same_binary_tree.py) | Trees | Solved | Recursively compare corresponding nodes in both trees | O(n) | O(h) |
| [Lowest Common Ancestor in Binary Search Tree](solutions/lowest_common_ancestor_in_binary_search_tree.py) | Trees | Solved | Follow BST ordering until the target paths split | O(h) | O(1) |
| [Binary Tree Level Order Traversal](solutions/binary_tree_level_order_traversal.py) | Trees | Solved | Breadth-first search with a queue grouped by level size | O(n) | O(w) |
| [Binary Tree Right Side View](solutions/binary_tree_right_side_view.py) | Trees | Solved | Right-first breadth-first search recording the first node at each level | O(n) | O(w) |
| [Count Good Nodes in Binary Tree](solutions/count_good_nodes_in_binary_tree.py) | Trees | Solved | Recursive DFS carrying the maximum value on the root-to-node path | O(n) | O(h) |
| [Valid Binary Search Tree](solutions/valid_binary_search_tree.py) | Trees | Solved | Recursive DFS carrying strict lower and upper bounds | O(n) | O(h) |
| [Kth Smallest Integer in BST](solutions/kth_smallest_integer_in_bst.py) | Trees | Solved | Recursive in-order traversal stored in a list | O(n) | O(n) |
| [Construct Binary Tree from Preorder and Inorder Traversal](solutions/construct_binary_tree_from_preorder_and_inorder_traversal.py) | Trees | Solved | Recursive reconstruction with preorder and inorder index boundaries | O(n) | O(n) |
| [Binary Tree Maximum Path Sum](solutions/binary_tree_maximum_path_sum.py) | Trees | Solved | Recursive DFS tracking upward gain and the best complete path | O(n) | O(h) |
| [Serialize and Deserialize Binary Tree](solutions/serialize_and_deserialize_binary_tree.py) | Trees | Solved | Preorder DFS with explicit null markers | O(n) | O(n) |
| [Implement Trie (Prefix Tree)](solutions/implement_trie_prefix_tree.py) | Tries | Solved | Character-to-child maps with end-of-word markers | O(L) per operation | O(total inserted characters) |
| [Design Add and Search Word Data Structure](solutions/design_add_and_search_word_data_structure.py) | Tries | Solved | Trie insertion with recursive wildcard search | O(L) add; O(26ᵈ × L) search | O(C + L) |
| [Word Search II](solutions/word_search_ii.py) | Tries | Solved | Trie-guided board backtracking with prefix pruning | O(S + rows × columns × 4ᴸ) | O(S + L) |
| [Kth Largest Element in a Stream](solutions/kth_largest_element_in_a_stream.py) | Heap / Priority Queue | Solved | Sort the stream in descending order after each addition | O(n log n) per addition | O(n) |
| [Last Stone Weight](solutions/last_stone_weight.py) | Heap / Priority Queue | Solved | Ascending sorted list with ordered reinsertion | O(n²) | O(1) |
| [K Closest Points to Origin](solutions/k_closest_points_to_origin.py) | Heap / Priority Queue | Solved | Size-k max-heap using negative squared distances | O(n log k) | O(k) |
| [Kth Largest Element in an Array](solutions/kth_largest_element_in_an_array.py) | Heap / Priority Queue | Solved | Size-k min-heap | O(n log k) | O(k) |
| [Task Scheduler](solutions/task_scheduler.py) | Heap / Priority Queue | Solved | Greedy max-heap with cooldown tracking | O(T + m log k) | O(k) |
| [Design Twitter](solutions/design_twitter.py) | Heap / Priority Queue | Solved | Collect and sort visible tweets by timestamp | O(v log v) per feed; O(1) average updates | O(p + f + v) |
| [Find Median From Data Stream](solutions/find_median_from_data_stream.py) | Heap / Priority Queue | Solved | Balanced max-heap and min-heap | O(log n) per addition; O(1) lookup | O(n) |
| [Subsets](solutions/subsets.py) | Backtracking | Solved | Include/exclude choice loop | O(n × 2ⁿ) | O(n × 2ⁿ) |
| [Subsets II](solutions/subsets_ii.py) | Backtracking | Solved | Sorted backtracking with a per-level processed dictionary | O(n × 2ⁿ) | O(n × 2ⁿ) |
| [Combination Sum](solutions/combination_sum.py) | Backtracking | Solved | Backtracking with sum pruning and a start index | O(nᵈ × d) | O(d + k × d) |
| [Combination Sum II](solutions/combination_sum_ii.py) | Backtracking | Solved | Sorted pop-based backtracking with same-level duplicate skipping | O(n × 2ⁿ) | O(n² + k × n) |
| [Permutations](solutions/permutations.py) | Backtracking | Solved | Backtracking with a copied remaining-numbers list | O(n × n!) | O(n² + n × n!) |
| [Generate Parentheses](solutions/generate_parentheses.py) | Backtracking | Solved | Insert pairs with explored-state pruning | O(n² × Cₙ) | O(n × Cₙ) |
| [Word Search](solutions/word_search.py) | Backtracking | Solved | Backtracking with prefix and visited-cell pruning | O(rows × columns × L × 4ᴸ) | O(L²) |
| [Palindrome Partitioning](solutions/palindrome_partitioning.py) | Backtracking | Solved | Backtracking with memoized palindrome checks | O(n × 2ⁿ) | O(n² + n × 2ⁿ) |
| [Letter Combinations of a Phone Number](solutions/letter_combinations_of_a_phone_number.py) | Backtracking | Solved | Digit-to-letters map with backtracking | O(n × 4ⁿ) | O(n × 4ⁿ) |
| [N-Queens](solutions/n_queens.py) | Backtracking | Solved | Row-by-row DFS with column and diagonal pruning | O(n! + S × n²) | O(n² + S × n²) |
| [Number of Islands](solutions/number_of_islands.py) | Graphs | Solved | Connected-component traversal over unvisited land nodes | O(rows × columns) | O(rows × columns) |
| [Max Area of Island](solutions/max_area_of_island.py) | Graphs | Solved | Connected-component traversal tracking the largest island | O(rows × columns) | O(rows × columns) |
| [Clone Graph](solutions/clone_graph.py) | Graphs | Solved | Breadth-first traversal with an original-to-copy node map | O(V + E) | O(V) |
| [Islands and Treasure](solutions/islands_and_treasure.py) | Graphs | Solved | Multi-source breadth-first search from every treasure | O(m × n) | O(m × n) |
| [Rotting Fruit](solutions/rotting_fruit.py) | Graphs | Solved | Multi-source breadth-first search grouped by minute | O(rows × columns) | O(rows × columns) |
| [Pacific Atlantic Water Flow](solutions/pacific_atlantic_water_flow.py) | Graphs | Solved | Reverse depth-first search from both oceans | O(rows × columns) | O(rows × columns) |
| [Surrounded Regions](solutions/surrounded_regions.py) | Graphs | Solved | Iterative DFS by connected O component with edge detection | O(rows × columns) | O(rows × columns) |
| [Course Schedule](solutions/course_schedule.py) | Graphs | Solved | Recursive DFS with three visitation states | O(V + E) | O(V + E) |
| [Course Schedule II](solutions/course_schedule_ii.py) | Graphs | Solved | DFS postorder with three visitation states | O(V + E) | O(V + E) |
| [Graph Valid Tree](solutions/graph_valid_tree.py) | Graphs | Solved | Recursive DFS with parent tracking and connectivity check | O(V + E) | O(V + E) |
| [Redundant Connection](solutions/redundant_connection.py) | Graphs | Solved | Adjacency matrix DFS with path-based cycle reconstruction | O(n²) | O(n²) |
| [Number of Connected Components in an Undirected Graph](solutions/number_of_connected_components_in_an_undirected_graph.py) | Graphs | Solved | Adjacency matrix with recursive DFS per component | O(n²) | O(n²) |
| [Word Ladder](solutions/word_ladder.py) | Graphs | Solved | Adjacency matrix with breadth-first search | O(n² × L) | O(n²) |
| [Network Delay Time](solutions/network_delay_time.py) | Graphs | Solved | Adjacency matrix with Dijkstra's algorithm | O(n² + E) | O(n²) |
| [Cheapest Flights Within K Stops](solutions/cheapest_flights_within_k_stops.py) | Graphs | Solved | Layered dynamic programming over the allowed flight count | O((k + 1) × (n + E)) | O((k + 2) × n) |
| [Reconstruct Flight Path](solutions/reconstruct_flight_path.py) | Graphs | Solved | Hierholzer's algorithm with destination min-heaps | O(E log E) | O(E) |
| [Min Cost to Connect Points](solutions/min_cost_to_connect_points.py) | Graphs | Solved | Kruskal's algorithm with Union-Find | O(n² log n) | O(n²) |
| [Swim in Rising Water](solutions/swim_in_rising_water.py) | Graphs | Solved | Dijkstra's algorithm with minimax path costs | O(n² log n) | O(n²) |
| [Alien Dictionary](solutions/alien_dictionary.py) | Graphs | Solved | DFS topological sort with three visitation states | O(C + V + E) | O(V + E) |
| [Climbing Stairs](solutions/climbing_stairs.py) | 1-D Dynamic Programming | Solved | Top-down recursion with memoization | O(n) | O(n) |
| [Min Cost Climbing Stairs](solutions/min_cost_climbing_stairs.py) | 1-D Dynamic Programming | Solved | Top-down recursion with memoization | O(n) | O(n) |
| [House Robber](solutions/house_robber.py) | 1-D Dynamic Programming | Solved | Top-down recursion with memoization | O(n) | O(n) |
| [House Robber II](solutions/house_robber_ii.py) | 1-D Dynamic Programming | Solved | Two linear ranges with top-down memoization | O(n) | O(n) |

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

### Reverse Nodes in K-Group

- Scan ahead from the previous group's boundary to confirm that k nodes remain.
- Leave the final nodes unchanged when that scan reaches the end early.
- Reverse a complete group by redirecting each node to its predecessor.
- Connect the previous group to the new head and the new tail to the next group.
- Relinking the existing nodes preserves their values and uses constant extra space.

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

### Invert Binary Tree

- An empty tree is the recursive base case and remains unchanged.
- Swap each node's left and right children, including when only one child exists.
- Recursively invert both swapped subtrees so every node in the tree is visited.
- The recursion stack uses O(h) space, where h is the tree height.

### Maximum Depth of Binary Tree

- An empty tree is the recursive base case and has depth zero.
- Recursively find the depths of the left and right subtrees.
- Choose the larger subtree depth because the answer follows the longest path.
- Add one to include the current node in that path.
- The recursion stack uses O(h) space, where h is the tree height.

### Diameter of Binary Tree

- Recursively calculate the maximum edge depth of each left and right subtree.
- A missing child has depth -1, making a leaf's depth zero and keeping all path lengths measured in edges.
- At every node, add the two child depths and two connecting edges to find the longest path through that node.
- Keep the largest path found because the tree's diameter does not need to pass through the root.
- The recursion stack uses O(h) space, where h is the tree height.

### Balanced Binary Tree

- An empty subtree is balanced and has height zero.
- Recursively obtain both the balance state and height of each child subtree.
- A node is balanced only when both child subtrees are balanced and their heights differ by at most one.
- Return the current height with the balance state so each node's height is calculated only once.
- The recursion stack uses O(h) space, where h is the tree height.

### Same Binary Tree

- Traverse both trees together so each recursive call compares corresponding nodes.
- Two missing nodes are equivalent, while exactly one missing node means the structures differ.
- When both nodes exist, their values and both pairs of child subtrees must match.
- The recursion stack uses O(h) space, where h is the height of the tree.

### Lowest Common Ancestor in Binary Search Tree

- When both target values are smaller than the current value, their lowest common ancestor must be in the left subtree.
- When both target values are larger than the current value, their lowest common ancestor must be in the right subtree.
- Otherwise, the target paths split at the current node, or the current node is one of the targets.
- Iteratively following only the shared search path takes O(h) time and O(1) extra space.

### Binary Tree Level Order Traversal

- A queue processes nodes in breadth-first order, preserving the left-to-right order within each level.
- Record the queue size before processing a level so children added during that iteration remain in the queue for the next level.
- Collect the values of exactly that many nodes, then append the completed level to the result.
- The queue uses O(w) space, where w is the maximum number of nodes at any level.

### Binary Tree Right Side View

- Process the tree one level at a time using breadth-first search.
- Add each right child before its left sibling so the next level is ordered from right to left.
- Record the node at the front of the queue before processing each level because it is the rightmost visible node.
- Capture the level size before adding children so each iteration processes exactly one level.
- The queue uses O(w) space, where w is the maximum number of nodes at any level.

### Count Good Nodes in Binary Tree

- Carry the largest value seen on the root-to-node path through each recursive DFS call.
- A node is good when its value is greater than or equal to the maximum from its ancestors.
- Update the path maximum before recursively visiting the current node's children.
- Every node is reached exactly once, so a visited set is unnecessary for a binary tree.
- The recursion stack uses O(h) space, where h is the height of the tree.

### Valid Binary Search Tree

- Recursive DFS can validate both the left and right subtrees.
- Each recursive call carries strict lower and upper bounds established by the node's ancestors.
- The current node becomes the upper bound for its left subtree and the lower bound for its right subtree.
- Duplicate values are invalid because the required inequalities are strict.
- The recursion stack uses O(h) space, where h is the height of the tree.

### Kth Smallest Integer in BST

- An in-order traversal visits a BST's values in ascending order.
- Recursively visit the left subtree, the current node, and then the right subtree.
- Append each visited value to a list.
- Because `k` is 1-indexed, return the value at list index `k - 1`.
- Storing all node values makes the approach easy to follow but uses O(n) space.

### Construct Binary Tree from Preorder and Inorder Traversal

- The first value in a preorder range is the root of that subtree.
- The root's inorder position separates the left and right subtree ranges.
- The number of values in the left inorder range identifies the matching preorder boundary.
- Index boundaries avoid copying traversal slices during recursive calls.

### Binary Tree Maximum Path Sum

- Recursively calculate the best single-branch gain from each child.
- Ignore a negative child gain because excluding it produces a larger path sum.
- A complete path through a node may combine both child gains with the node's value.
- The gain returned to a parent uses at most one child because the path cannot branch again.
- Initialize the global maximum below every possible node value so all-negative trees are handled correctly.

### Serialize and Deserialize Binary Tree

- A preorder traversal writes each node before its left and right subtrees.
- An explicit null marker preserves missing children and therefore the exact tree structure.
- `join` combines the recorded values into one string, and `split` restores the value tokens.
- During deserialization, a shared index advances once per value or null marker.
- Each node is processed once, so serialization and deserialization both take O(n) time.

### Implement Trie (Prefix Tree)

- Each node maps characters to child nodes, allowing words with the same prefix to share a path.
- Insertion creates only the missing nodes while following a word from the root.
- An end-of-word marker distinguishes a complete inserted word from a path that is only a prefix.
- `search` requires both a complete path and an end marker, while `startsWith` requires only the path.
- Processing a word or prefix of length `L` takes O(L) time.

### Design Add and Search Word Data Structure

- Words with common prefixes share trie nodes, while end markers distinguish
  complete words from prefixes.
- A normal search letter follows one child path.
- A dot recursively tries every child path until one produces a complete
  match.
- Reaching the end of the query succeeds only at an end-of-word marker.
- In the worst case, a search with `d` dots takes O(26ᵈ × L) time and uses
  O(L) recursive stack space.

### Word Search II

- Store all candidate words in a trie so words with common prefixes share the same path.
- Start backtracking from every board cell and move only horizontally or vertically.
- Track visited positions so one search path cannot reuse a board cell.
- Follow the trie node that matches the current cell and prune the branch immediately when no matching child exists.
- Store complete words at terminal trie nodes and clear each one after finding it so multiple board paths cannot add duplicate results.
- If `S` is the total number of word characters and `L` is the longest word length, the worst-case time is O(S + rows × columns × 4ᴸ), while the trie and active search use O(S + L) auxiliary space.

### Kth Largest Element in a Stream

- Sort the stream from largest to smallest so the kth largest value is stored at index `k - 1`.
- Each call to `add` appends the new value and restores the descending order before returning the result.
- Repeated values count as separate positions in the sorted order.
- Sorting the complete stream makes each addition O(n log n), while storing all values uses O(n) space.

### Last Stone Weight

- Sort the stones in increasing order so the two heaviest stones are at the end.
- Remove those two stones and calculate the heavier weight minus the lighter weight.
- Reinsert a positive difference in its correct sorted position; equal stones leave nothing to reinsert.
- Continue until zero or one stone remains, then return zero or the remaining weight.
- Ordered list insertion can shift O(n) elements per smash, producing O(n²) time and O(1) auxiliary space.

### K Closest Points to Origin

- Squared distance preserves the same ordering as Euclidean distance, so calculating a square root is unnecessary.
- Store negative distances to simulate a max-heap using Python's min-heap operations.
- Keep at most k points in the heap by removing the farthest point whenever its size exceeds k.
- After every point has been processed, the heap contains the k closest points in any order.

### Kth Largest Element in an Array

- Keep only the k largest values encountered so far in a min-heap.
- When the heap grows beyond size k, remove its smallest value.
- Duplicate values count as separate positions in the sorted order.
- After traversal, the heap's smallest value is the kth largest overall.

### Task Scheduler

- Among tasks that are ready, prefer the task with the largest remaining count.
- A cooldown queue records when a previously run task becomes available again.
- A task run at time `t` can next run at time `t + n + 1`.
- A cycle is idle only when every unfinished task is cooling down.
- With `m` tasks, `k` task types, and `T` total cycles, simulation takes O(T + m log k) time and O(k) space.

### Design Twitter

- Map each user ID to that user's tweets and each follower ID to a set of direct followees.
- Pair every tweet ID with a global timestamp because tweet IDs do not represent publication order.
- A user's feed includes their own tweets and tweets authored by users they directly follow.
- Following is not transitive, and a set prevents duplicate follow relationships.
- Collect and sort all `v` visible tweets, then return the first 10 IDs in newest-first order.
- With `p` stored tweets and `f` follow relationships, storage is O(p + f); building a feed temporarily uses O(v) more space.

### Find Median From Data Stream

- Keep the smaller half of the stream in a max-heap and the larger half in a min-heap.
- Negate values in the smaller heap because Python's `heapq` implements a min-heap.
- Rebalance after every insertion so the smaller heap has either the same size as the larger heap or one extra value.
- For an odd count, the smaller heap's maximum is the median; for an even count, average both heap tops.

### Subsets

- At each index, a `for` loop tries the two choices: include the current number or exclude it.
- A subset becomes complete and valid after every input number has received a choice.
- Only complete subsets are copied into the result at the base case.
- After exploring an inclusion, remove that number to undo the choice before trying exclusion.
- Exclusion changes nothing in the current subset, so there is nothing to undo for that choice.
- There are `2ⁿ` subsets, and copying subsets makes the total time and returned-output space O(n × 2ⁿ).
- The current subset and recursion stack use O(n) auxiliary space when the returned output is excluded.

### Subsets II

- Every partial subset is valid, so copy it into the result at the start of each recursive call.
- Sort a copy of the input so every generated subset has one consistent value order without changing the caller's list.
- Create a new processed-values dictionary for each recursion level and skip a value already explored by a sibling branch.
- A fresh dictionary in deeper calls still allows repeated values within a subset, such as `[7, 7]`.
- Recurse from the index after the chosen occurrence so each array element can be selected at most once.
- Producing and copying all subsets takes O(n × 2ⁿ) time and output space; the current subset, recursion stack, sorted copy, and live dictionaries use O(n) auxiliary space.

### Combination Sum

- A value from `nums` may appear multiple times in one combination.
- Combination order and value order do not affect uniqueness; only the frequency of each chosen value matters.
- Track the current sum so a branch can be recorded at `target` or pruned after exceeding `target`.
- Restrict choices to the current `start_index` and later positions to avoid generating different orderings of the same combination.
- Recurse with the chosen index, rather than the next index, to allow the chosen number to be reused.
- If `d = target // min(nums)` and `k` combinations are returned, the worst-case time is O(nᵈ × d), auxiliary space is O(d), and output space is O(k × d).

### Combination Sum II

- Sort a copy of the candidates so duplicate values are adjacent without modifying the caller's input.
- Give each recursive branch its own remaining-candidates list so popping a value does not affect sibling branches.
- Passing only the candidates left after a pop ensures each candidate occurrence can be chosen at most once.
- Skip a value when it equals the previous choice at the same recursion level, preventing duplicate combinations.
- Remove the chosen value from the current state after recursion so the next branch starts from the correct state.
- Copying candidate lists throughout an exponential search takes O(n × 2ⁿ) time and O(n²) auxiliary stack space; `k` results use up to O(k × n) output space.

### Permutations

- Each recursion level chooses the number that will occupy the next position in the current permutation.
- Give every branch its own remaining-numbers list, then remove the chosen number so it cannot be reused in that permutation.
- Copy a complete current state into the result because the state list is mutable and will be changed during backtracking.
- Remove the last choice after recursion so the next branch starts from the correct state.
- No pruning is needed because every partial permutation can be completed with the remaining unique numbers.
- Returning all `n!` permutations requires O(n × n!) time and output space; copied remaining lists use O(n²) auxiliary space along one recursion path.

### Generate Parentheses

- Begin with the empty string and insert a complete `()` pair at every possible position.
- Inserting a well-formed pair into a well-formed string preserves well-formedness, so every explored state remains valid.
- Different insertion positions or branches can create the same string, so an explored set prunes duplicate states before recursion.
- A state containing `n` pairs is complete and can be added directly to the result.
- If `Cₙ` is the nth Catalan number, creating and checking insertion candidates takes O(n² × Cₙ) time, while stored states use O(n × Cₙ) space.

### Word Search

- Try every board position because any cell may begin the word.
- Track the current row and column so each branch can explore the four horizontal and vertical neighbors.
- Prune a branch when its chosen letter does not match `word[len(current_state)]`.
- Add each chosen position to a visited set so one path cannot reuse a cell, then remove it while backtracking.
- If `L` is the word length, the search takes O(rows × columns × L × 4ᴸ) time because extending immutable strings costs up to O(L).
- The visited set and recursion stack use O(L) space; simultaneous immutable string states use O(L²) space.

### Palindrome Partitioning

- Track a start index so the current partition always covers one continuous prefix of the input.
- Try every right boundary for the next substring and recurse only when that substring is a palindrome.
- Continue after a failed palindrome check because adding another character may produce a palindrome.
- Memoize checks by inclusive `(left, right)` boundaries so each substring range is evaluated once.
- Copy the current partition only after its substrings cover the complete input, then remove the last choice while backtracking.
- In the worst case, returning exponentially many partitions takes O(n × 2ⁿ) time and output space; the palindrome cache uses O(n²) auxiliary space.

### Letter Combinations of a Phone Number

- Each input digit contributes one character from its telephone-keypad mapping.
- Track the digit index so each recursion level chooses one letter for the next position.
- Add a complete combination after one letter has been chosen for every digit.
- Remove the last chosen letter after recursion so the next branch can reuse the current state.
- An empty input returns an empty list.
- In the worst case, there are 4ⁿ strings of length `n`, requiring O(n × 4ⁿ) time and output space; the recursion uses O(n) auxiliary space.

### N-Queens

- Treat the board as a layered search graph where each layer is one row and each node is a possible queen position.
- Moving to the next layer places exactly one queen per row, so horizontal conflicts are prevented automatically.
- Track occupied columns, `row + column` diagonals, and `row - column` diagonals in sets for constant-time conflict checks.
- Prune a branch immediately when a new queen conflicts with a previously placed queen.
- Reaching row `n` completes a valid path; convert the mutable board to strings and add that layout to the result.
- Undo every placement and its occupied markers before exploring another column.
- The search takes O(n! + S × n²) time, where `S` is the number of solutions; the board uses O(n²) auxiliary space and the returned layouts use O(S × n²) space.

### Number of Islands

- Treat every land cell as a graph node, with edges to horizontal and vertical land neighbors.
- Store all unprocessed land positions in a set; water cells are excluded from the graph.
- Starting from any unvisited land node, an iterative depth-first traversal removes its entire connected component from the set.
- Increment the island count once before traversing each new component, rather than at traversal dead ends.
- Continue until the unvisited-land set is empty; each completed traversal represents exactly one island.
- Building and traversing the land-node set takes O(rows × columns) time and O(rows × columns) space.

### Max Area of Island

- Reuse the connected-component traversal from Number of Islands.
- Treat every land cell as a graph node, with edges to horizontal and vertical land neighbors.
- Store all unprocessed land positions in a set; water cells are excluded from the graph.
- Starting from any unvisited land node, an iterative depth-first traversal removes its entire connected component from the set.
- Instead of counting components, count the land cells visited in the current component.
- Record the maximum component area after each traversal finishes.
- Building and traversing the land-node set takes O(rows × columns) time and O(rows × columns) space.

### Clone Graph

- A deep copy must preserve every node value and neighbor relationship.
- Every node in the returned graph must be a new object; no copied neighbor may point to an original node.
- The empty graph is represented by `None`, while `[[]]` represents one node with no neighbors.
- Map each original node object to exactly one copied node so cycles and shared neighbors do not create duplicate copies.
- Add an original node to the BFS queue only when its copy is first created.
- While processing each original edge, append the copied neighbor to the current copied node's neighbor list.
- Visiting each node and edge takes O(V + E) time; the map and queue use O(V) auxiliary space.

### Islands and Treasure

- Water cells cannot be traversed, and movement is limited to horizontal and vertical neighbors.
- Each land cell must store its distance to the nearest treasure chest.
- Land that cannot reach a treasure chest remains unchanged.
- Add every treasure to the queue before starting so breadth-first search expands from all sources simultaneously.
- Assign a distance only when an `INF` cell is first reached; BFS guarantees that this is its shortest distance.
- Every cell is processed at most once, giving O(m × n) time and O(m × n) queue space.

### Rotting Fruit

- Empty cells do not contain fruit and do not spread rot.
- Fresh fruit changes only when it is horizontally or vertically adjacent to rotten fruit.
- Return the elapsed minutes when no fresh fruit remains, or `-1` if some fresh fruit cannot rot.
- Add every initially rotten fruit to the queue so breadth-first search starts from all sources simultaneously.
- Process one queue layer per minute and place newly rotten fruit in the next minute's queue.
- Increment the timer only when at least one fresh fruit becomes rotten.
- Every cell is scanned or processed a constant number of times, giving O(rows × columns) time and queue space.

### Pacific Atlantic Water Flow

- Treat every island cell as a graph node with edges to its horizontal and vertical neighbors.
- Start one multi-source depth-first search from the top and left Pacific borders.
- Start another multi-source depth-first search from the bottom and right Atlantic borders.
- Reverse the water-flow direction by moving from each ocean toward neighboring cells of equal or greater height.
- Keep a visited set for each ocean so every cell is processed at most once by that search.
- Cells in the intersection of the two visited sets can send water to both oceans.
- The two searches take O(rows × columns) time and O(rows × columns) auxiliary space.

### Surrounded Regions

- Only horizontal and vertical neighbors belong to the same region.
- A region is captured only when none of its `"O"` cells touch an edge of the board.
- Every `"O"` in a captured region must be changed to `"X"` in place.
- Edge-connected `"O"` regions must remain unchanged.
- Use iterative DFS to collect each connected `"O"` component and record whether any cell touches an edge.
- After a component has been fully explored, change its cells only when its edge flag is false.
- The board scan and DFS take O(rows × columns) time; the visited set, stack, and component list use O(rows × columns) space.

### Course Schedule

- Courses are labeled from `0` through `numCourses - 1`.
- A prerequisite pair `[a, b]` means course `b` must be completed before course `a`.
- Build a directed adjacency list with an edge from each prerequisite to the course that depends on it.
- Mark a course as visiting while it is on the current DFS path and visited only after all courses reachable from it are safely processed.
- Reaching a visiting course proves there is a cycle, while reaching a visited course is safe because its paths were already checked.
- Start DFS from every unvisited course so disconnected graph components are also checked.
- Building and traversing the graph takes O(V + E) time; the adjacency list, states, and recursion stack use O(V + E) space.

### Course Schedule II

- A valid result is a topological ordering containing every course exactly once.
- Reuse the three DFS states from Course Schedule to detect cycles.
- Append a course only after every dependent course reachable from it has been processed.
- This produces reverse topological order, so reverse the completed list before returning it.
- If DFS finds a cycle, no valid ordering exists, so return an empty list.
- Start DFS from every unvisited course so disconnected courses are also included.
- Building and traversing the graph takes O(V + E) time; the graph, state list, result, and recursion stack use O(V + E) space.

### Graph Valid Tree

- Nodes are labeled from `0` through `n - 1`.
- Build an adjacency list in both directions because every edge is undirected.
- During DFS, skip the edge leading back to the current node's parent.
- Reaching any other visited node identifies a cycle.
- After DFS, every node must be visited; otherwise, the graph has multiple connected components.
- Building and traversing the graph takes O(V + E) time and O(V + E) space.

### Redundant Connection

- The input is a tree with exactly one additional undirected edge.
- Removing the redundant edge must leave the graph connected and without a cycle.
- Build an undirected adjacency matrix and use DFS to find the cycle.
- Track the current DFS path and each node's position so reaching a node still on that path identifies all cycle edges.
- Normalize cycle edges so their endpoint order does not affect membership checks.
- Scan the original edge list backward and return the first edge that belongs to the cycle.
- The adjacency matrix and neighbor scans take O(n²) time and O(n²) space.

### Number of Connected Components in an Undirected Graph

- Nodes are labeled from `0` through `n - 1`.
- Each edge connects two nodes in both directions because the graph is undirected.
- Nodes connected by a path belong to the same component.
- A node without any edges forms a component by itself.
- Mark each node as processed when DFS first visits it so cycles do not repeat work.
- Start a new DFS from every remaining unprocessed node and increment the component count once for each new search.
- The adjacency matrix and scanning every possible neighbor take O(n²) time and O(n²) space.

### Word Ladder

- Every word has the same length and contains only lowercase English letters.
- Each transformation must produce a word from `wordList` that differs at exactly one character position.
- The returned length counts every word in the sequence, including `beginWord` and `endWord`.
- Return `0` when no valid sequence reaches `endWord`.
- Treat each distinct word as a graph node and connect two nodes when their words differ at exactly one position.
- Include `beginWord` as the source node even when it does not appear in `wordList`.
- Because every edge represents one transformation, breadth-first search finds the minimum number of transformations without Dijkstra's priority queue.
- Add one to the shortest edge distance to count the words in the transformation sequence.
- Comparing every pair of length-L words takes O(n² × L) time; the adjacency matrix uses O(n²) space.

### Network Delay Time

- Nodes are labeled from `1` through `n`, and every edge has a direction and a nonnegative travel time.
- The signal begins at node `k` at time zero.
- The result is the earliest time by which every node has received the signal.
- Return `-1` when any node is unreachable from the source.
- Store directed travel times in an adjacency matrix, using infinity to distinguish missing edges from zero-weight edges.
- Dijkstra's algorithm repeatedly selects the unvisited node with the smallest known distance and relaxes its outgoing edges.
- Return the maximum shortest-path distance because that is when the final reachable node receives the signal.
- Scanning the matrix takes O(n² + E) time, and the matrix uses O(n²) space.

### Cheapest Flights Within K Stops

- At most `k` intermediate stops means a route may use at most `k + 1` flights.
- Row `i` of the DP table stores the cheapest cost to every airport using at most `i` flights.
- Copy the preceding row first so routes using fewer flights remain available in every later row.
- Relax each directed flight using only costs from the preceding row, preventing one iteration from adding multiple flights.
- The destination needs no special update because it is processed like every other target airport and read from the final row.
- Processing every airport copy and every flight for `k + 1` layers takes O((k + 1) × (n + E)) time, while retaining all `k + 2` rows uses O((k + 2) × n) space.

### Reconstruct Flight Path

- The itinerary starts at `"JFK"` and contains one more airport than the number of tickets.
- Every supplied ticket must be used exactly once, including duplicate tickets.
- When several complete flight paths are valid, return the lexicographically smallest itinerary.
- The problem guarantees that at least one valid flight path exists.
- Store each airport's destinations in a min-heap so the smallest available destination is removed first.
- Hierholzer's algorithm consumes each ticket while moving forward and appends airports while backtracking.
- Reverse the postorder route so early dead ends appear in their valid final positions.
- Heap insertion and removal take O(E log E) total time; the graph, recursion stack, and route use O(E) space.

### Min Cost to Connect Points

- Each point is a distinct coordinate pair on a 2D plane.
- The cost of a direct connection is the Manhattan distance between its two points.
- The result must connect every point with exactly one simple path between each pair.
- A single point requires no connections and therefore has a total cost of zero.
- Create the complete graph by calculating an edge for every pair of points, then sort those edges by cost.
- Kruskal's algorithm accepts an edge only when its endpoints belong to different selected-edge groups.
- Union-Find uses path compression and union by rank to merge groups and detect cycle-forming edges efficiently.
- Stop after selecting `n - 1` edges because a spanning tree on `n` points has exactly that many edges.
- Creating O(n²) edges and sorting them takes O(n² log n) time; storing the edges takes O(n²) space.

### Swim in Rising Water

- Treat each grid cell as a graph node connected to its horizontal and vertical neighbors.
- A path becomes usable when the water reaches the highest elevation encountered on that path.
- Moving to a neighbor therefore changes the required time to the maximum of the current path time and the neighbor's elevation.
- Dijkstra's algorithm uses a min-heap to process the cell with the smallest known required time.
- Keep the smallest known time for each cell and ignore stale heap entries after a better route is found.
- The first removal of the bottom-right cell from the heap gives the minimum possible time.
- Processing O(n²) cells and their heap operations takes O(n² log n) time; the heap and best-time matrix use O(n²) space.

### Alien Dictionary

- Include every unique letter as a graph node, even when no comparison creates an edge for it.
- Compare neighboring words and use only their first different letters to establish the directed ordering edge.
- A longer word appearing before its own prefix makes the supplied dictionary order invalid.
- Use three DFS states to distinguish unvisited letters, letters on the current path, and completely processed letters.
- Reaching a letter on the current path identifies a cycle and means no alien alphabet can satisfy the relationships.
- Append each letter after its outgoing neighbors and reverse the postorder to produce a valid topological ordering.
- Reading the input and traversing the graph takes O(C + V + E) time; the graph, states, result, and recursion stack use O(V + E) space.

### Climbing Stairs

- Each move climbs either one or two steps.
- Ways with a different sequence of moves count as distinct.
- Every path ending in one step extends a valid path to `n - 1`.
- Every path ending in two steps extends a valid path to `n - 2`.
- These groups have different final moves, so their counts can be added.
- Memoization stores each smaller result so it is calculated only once.
- The base cases are one way for `n = 1` and two ways for `n = 2`.
- Calculating and caching each value through `n` takes O(n) time and O(n) space, including the recursion stack.

### Min Cost Climbing Stairs

- Each indexed step has a cost that is paid when that step is used.
- A move climbs either one or two steps.
- The climb may begin at step 0 or step 1.
- The top is the position immediately beyond the final indexed step.
- To reach floor `n`, the final move comes from floor `n - 1` or floor `n - 2`.
- Add the cost of the departure step to the minimum cost of reaching that step.
- Floors 0 and 1 both have an initial cost of zero because the climb may start at either one.
- Memoization calculates each floor once, producing O(n) time and O(n) space.

### House Robber

- At each house, either skip it or rob it and skip the adjacent previous house.
- Skipping index `n` keeps the best result through index `n - 1`.
- Robbing index `n` adds `nums[n]` to the best result through index `n - 2`.
- Take the larger of these two choices for every index.
- An index below zero contributes no money, while index 0 contributes `nums[0]`.
- Memoization calculates each index once, producing O(n) time and O(n) space.

### House Robber II

- The first and last houses cannot both be robbed because the houses form a circle.
- Excluding the last house produces the linear range from index 0 through `n - 2`.
- Excluding the first house produces the linear range from index 1 through `n - 1`.
- Solve both ranges with the House Robber recurrence and take the larger result.
- Memo keys include the starting boundary so results from the two ranges remain distinct.
- The single-house input is handled separately because both reduced ranges would otherwise be empty.
- The two linear solves take O(n) time and O(n) space in total.
