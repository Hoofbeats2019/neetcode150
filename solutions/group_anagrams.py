"""Group Anagrams.

Group strings that contain the same characters with the same frequencies.

Example: groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
returns [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].
"""

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    """Use each string's sorted characters as its anagram-group key."""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: DefaultDict[str, List[str]] = defaultdict(list)
        for word in strs:
            groups["".join(sorted(word))].append(word)
        return list(groups.values())


def test_worked_example() -> None:
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert {tuple(group) for group in result} == {("eat", "tea", "ate"), ("tan", "nat"), ("bat",)}


if __name__ == "__main__":
    test_worked_example()
    print("The worked example passed.")
