"""Evaluate Reverse Polish Notation."""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}: stack.append(int(token)); continue
            right, left = stack.pop(), stack.pop()
            if token == "+": stack.append(left + right)
            elif token == "-": stack.append(left - right)
            elif token == "*": stack.append(left * right)
            else: stack.append(int(left / right))
        return stack[-1]
