"""Longest Substring Without Repeating Characters."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index: dict[str, int] = {}
        left = best = 0
        for right, character in enumerate(s):
            if character in last_index and last_index[character] >= left:
                left = last_index[character] + 1
            last_index[character] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    print("The worked example passed.")
