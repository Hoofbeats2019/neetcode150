"""Longest Repeating Character Replacement."""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: dict[str, int] = {}
        left = max_count = best = 0
        for right, character in enumerate(s):
            counts[character] = counts.get(character, 0) + 1
            max_count = max(max_count, counts[character])
            while right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
