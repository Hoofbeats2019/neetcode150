"""Valid Parentheses."""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []
        for character in s:
            if character in pairs:
                if not stack or stack.pop() != pairs[character]: return False
            else: stack.append(character)
        return not stack
