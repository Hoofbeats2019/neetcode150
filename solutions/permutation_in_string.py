"""Permutation in String."""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        needed, window = Counter(s1), Counter(s2[:len(s1)])
        if window == needed: return True
        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1
            left = s2[right - len(s1)]
            window[left] -= 1
            if window[left] == 0: del window[left]
            if window == needed: return True
        return False
