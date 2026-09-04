"""Minimum Window Substring."""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = Counter(t), {}
        formed = left = 0
        best = (float("inf"), 0, 0)
        for right, char in enumerate(s):
            have[char] = have.get(char, 0) + 1
            if char in need and have[char] == need[char]: formed += 1
            while formed == len(need):
                if right - left + 1 < best[0]: best = (right - left + 1, left, right)
                removed = s[left]
                have[removed] -= 1
                if removed in need and have[removed] < need[removed]: formed -= 1
                left += 1
        return "" if best[0] == float("inf") else s[best[1]:best[2]+1]
