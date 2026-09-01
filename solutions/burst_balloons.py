"""Burst Balloons.

Created: 1 September 2026
Created by: Yanlong Su

Given an integer array ``nums``, each element represents a balloon. Bursting
balloon ``i`` earns ``nums[i - 1] * nums[i] * nums[i + 1]`` coins, where an
out-of-bounds neighbor has value ``1``. Return the maximum coins obtainable by
bursting every balloon.

Example 1:
    Input: nums = [4, 2, 3, 7]
    Output: 143
    Explanation: Burst 2, then 3, then 4, then 7 for
                 4 * 2 * 3 + 4 * 3 * 7 + 1 * 4 * 7 + 1 * 7 * 1 = 143.

Constraints:
    1 <= len(nums) <= 300
    0 <= nums[i] <= 100

Pseudocode:
    maxCoins(nums):
        add a virtual balloon with value 1 to both ends
        create an empty memo

        dfs(left, right):
            if no balloons exist strictly between left and right:
                return 0
            if (left, right) is memoized:
                return its result

            best = 0
            for each k strictly between left and right:
                choose k as the last balloon burst in this interval
                coins = balloons[left] * balloons[k] * balloons[right]
                best = max(best, dfs(left, k) + coins + dfs(k, right))

            memoize and return best

        return dfs(0, final index)

Time complexity: O(n^3)
Space complexity: O(n^2)
"""


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """Return the maximum coins from bursting every balloon."""
        balloons = [1] + nums + [1]
        memo: dict[tuple[int, int], int] = {}

        def dfs(left: int, right: int) -> int:
            if right - left == 1:
                return 0

            state = (left, right)

            if state in memo:
                return memo[state]

            best = 0

            for last_burst in range(left + 1, right):
                coins_from_last_burst = (
                    balloons[left] * balloons[last_burst] * balloons[right]
                )
                total_coins = (
                    dfs(left, last_burst)
                    + coins_from_last_burst
                    + dfs(last_burst, right)
                )
                best = max(best, total_coins)

            memo[state] = best
            return best

        return dfs(0, len(balloons) - 1)


def test_example_1() -> None:
    """Run the supplied worked example."""
    assert Solution().maxCoins([4, 2, 3, 7]) == 143


if __name__ == "__main__":
    test_example_1()
    print("All example tests passed.")
