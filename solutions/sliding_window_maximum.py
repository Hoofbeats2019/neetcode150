"""Sliding Window Maximum."""
from collections import deque
from typing import Deque, List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexes: Deque[int] = deque()
        result: List[int] = []
        for right, value in enumerate(nums):
            while indexes and indexes[0] <= right - k: indexes.popleft()
            while indexes and nums[indexes[-1]] <= value: indexes.pop()
            indexes.append(right)
            if right >= k - 1: result.append(nums[indexes[0]])
        return result
