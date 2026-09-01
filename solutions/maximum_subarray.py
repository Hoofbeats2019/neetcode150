"""Maximum Subarray.

Created: 1 September 2026
Created by: Yanlong Su

Given an integer array ``nums``, find the contiguous, non-empty subarray with
the largest sum and return that sum.

Example 1:
    Input: nums = [2, -3, 4, -2, 2, 1, -1, 4]
    Output: 8
    Explanation: The subarray ``[4, -2, 2, 1, -1, 4]`` has the largest sum, 8.

Example 2:
    Input: nums = [-1]
    Output: -1

Constraints:
    1 <= len(nums) <= 100,000
    -10,000 <= nums[i] <= 10,000

Pseudocode:
    bestSum = nums[0]
    currentSum = nums[0]

    for each number from nums[1] onward:
        currentSum = maximum(number, currentSum + number)
        bestSum = maximum(bestSum, currentSum)

    return bestSum

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the largest sum of any contiguous, non-empty subarray."""
        best_sum = nums[0]
        current_sum = nums[0]

        for number in nums[1:]:
            current_sum = max(number, current_sum + number)
            best_sum = max(best_sum, current_sum)

        return best_sum


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().maxSubArray([2, -3, 4, -2, 2, 1, -1, 4]) == 8


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().maxSubArray([-1]) == -1


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
