"""Maximum Product Subarray.

Created: 26 August 2026
Created by: Yanlong Su

Given an integer array ``nums``, find a contiguous, non-empty subarray with
the largest product and return that product.

The product of a single-element subarray is the value of that element.

Example 1:
    Input: nums = [2, 4, -3, 5]
    Output: 8
    Explanation: The subarray ``[2, 4]`` has the largest product, 8.

Example 2:
    Input: nums = [-3, 0, -2]
    Output: 0
    Explanation: ``[-3, -2]`` is not contiguous, so it is not a subarray.

Constraints:
    1 <= len(nums) <= 20,000
    -10 <= nums[i] <= 10
    The product of every subarray fits in a 32-bit integer.

Pseudocode:
    maxProduct(nums):
        set maximum ending, minimum ending, and best to nums[0]

        for each number after nums[0]:
            save the previous maximum and minimum ending products

            set maximum ending to the largest of:
                the current number
                current number * previous maximum ending
                current number * previous minimum ending

            set minimum ending to the smallest of the same three products
            update best with the maximum ending product

        return best

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Return the largest product of any contiguous subarray."""
        maximum_ending = nums[0]
        minimum_ending = nums[0]
        largest_product = nums[0]

        for index in range(1, len(nums)):
            number = nums[index]
            previous_maximum = maximum_ending
            previous_minimum = minimum_ending

            maximum_ending = max(
                number,
                number * previous_maximum,
                number * previous_minimum,
            )
            minimum_ending = min(
                number,
                number * previous_maximum,
                number * previous_minimum,
            )
            largest_product = max(largest_product, maximum_ending)

        return largest_product


def test_example_1() -> None:
    """Run the first worked example."""
    assert Solution().maxProduct([2, 4, -3, 5]) == 8


def test_example_2() -> None:
    """Run the second worked example."""
    assert Solution().maxProduct([-3, 0, -2]) == 0


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    print("Both example tests passed.")
