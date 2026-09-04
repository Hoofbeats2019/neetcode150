"""Encode and Decode Strings.

Encode a list of arbitrary strings into one string, then decode it without
losing boundaries or characters.
"""

from typing import List


class Solution:
    """Prefix each string with its length and a delimiter."""

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, encoded: str) -> List[str]:
        result: List[str] = []
        index = 0
        while index < len(encoded):
            delimiter = encoded.index("#", index)
            length = int(encoded[index:delimiter])
            start = delimiter + 1
            result.append(encoded[start : start + length])
            index = start + length
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.decode(solution.encode(["neet", "code", "#"])) == ["neet", "code", "#"]
    print("The worked example passed.")
